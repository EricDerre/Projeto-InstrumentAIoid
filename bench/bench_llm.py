"""Benchmark de LLM no Ollama: CPU (num_gpu=0) x GPU, prefill e geracao separados.
Uso: python bench_llm.py [rotulo_cenario]   -> grava resultados/llm_<rotulo>.jsonl
"""
import json, subprocess, sys, time, pathlib, statistics as st
import requests

URL = "http://localhost:11434"
CENARIO = sys.argv[1] if len(sys.argv) > 1 else "sem_jogo"
MODELOS = ["qwen3:1.7b", "llama3.2:3b", "ministral-3:3b", "qwen3:4b", "qwen2.5:7b", "R4C3R/qwen3-8b-heretic:Q4_K_M"]
if len(sys.argv) > 2:
    MODELOS = sys.argv[2].split(",")
PERSONA = ("Voce e a Astolfo, uma assistente virtual animada e brincalhona que canta, toca "
           "instrumentos e joga videogame com o usuario. Responda sempre em portugues do Brasil, "
           "em no maximo duas frases curtas, com personalidade.")
PERGUNTAS = ["Oi! Tudo bem? O que voce gosta de fazer?",
             "Estou perdendo nessa fase, alguma dica rapida?",
             "Canta um pedacinho de uma musica pra mim?"]
MODOS = {"cpu": {"num_gpu": 0, "num_thread": 8}, "gpu": {}}

out = pathlib.Path(__file__).resolve().parent / "resultados"; out.mkdir(exist_ok=True)
arq = out / f"llm_{CENARIO}.jsonl"


def vram_usada_mb():
    try:
        r = subprocess.run(["nvidia-smi", "--query-gpu=memory.used", "--format=csv,noheader,nounits"],
                           capture_output=True, text=True, timeout=10)
        return int(r.stdout.strip().splitlines()[0])
    except Exception:
        return None


def descarregar(m):
    requests.post(f"{URL}/api/generate", json={"model": m, "keep_alive": 0}, timeout=120)
    time.sleep(2)


def chat(m, opts, pergunta):
    body = {"model": m, "stream": False, "think": False, "keep_alive": "5m",
            "messages": [{"role": "system", "content": PERSONA}, {"role": "user", "content": pergunta}],
            "options": {"num_ctx": 4096, "num_predict": 80, "temperature": 0.7, **opts}}
    t = time.time()
    r = requests.post(f"{URL}/api/chat", json=body, timeout=600)
    if r.status_code != 200 and "think" in r.text:
        body.pop("think"); r = requests.post(f"{URL}/api/chat", json=body, timeout=600)
    r.raise_for_status(); d = r.json(); d["_parede_s"] = time.time() - t
    return d


for m in MODELOS:
    for modo, opts in MODOS.items():
        descarregar(m)
        vram0 = vram_usada_mb()
        try:
            aquec = chat(m, opts, "Diga ola.")
        except Exception as e:
            print(m, modo, "ERRO", e); continue
        ps = requests.get(f"{URL}/api/ps").json().get("models", [])
        info = next((x for x in ps if x["name"] == m or x["model"] == m), {})
        vram1 = vram_usada_mb()
        pre, ger, parede, txt = [], [], [], []
        for p in PERGUNTAS:
            d = chat(m, opts, p)
            if d.get("prompt_eval_duration"):
                pre.append(d["prompt_eval_count"] / (d["prompt_eval_duration"] / 1e9))
            ger.append(d["eval_count"] / (d["eval_duration"] / 1e9))
            parede.append(d["_parede_s"]); txt.append(d["message"]["content"][:200])
        reg = {"cenario": CENARIO, "modelo": m, "modo": modo,
               "carga_s": round(aquec.get("load_duration", 0) / 1e9, 2),
               "prefill_tok_s": round(st.median(pre), 1) if pre else None,
               "geracao_tok_s": round(st.median(ger), 1),
               "resposta_s_mediana": round(st.median(parede), 2),
               "tam_mb": round(info.get("size", 0) / 2**20), "vram_modelo_mb": round(info.get("size_vram", 0) / 2**20),
               "vram_delta_nvsmi_mb": (vram1 - vram0) if vram0 is not None and vram1 is not None else None,
               "amostra": txt[0]}
        print(json.dumps(reg, ensure_ascii=False))
        with open(arq, "a", encoding="utf-8") as f:
            f.write(json.dumps(reg, ensure_ascii=False) + "\n")
    descarregar(m)
