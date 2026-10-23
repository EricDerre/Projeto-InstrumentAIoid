"""RAM e velocidade do LLM no Ollama variando mmap, contexto, cache KV e quantizacao (so CPU).
Uso: python bench_ram_llm.py <porta> <rotulo> <modelo1,modelo2> [opcoes_json]
Mede o processo llama-server.exe (o motor que o Ollama sobe) depois de uma resposta curta.
"""
import json, sys, time, pathlib, statistics as st
import psutil, requests

B = pathlib.Path(__file__).resolve().parent
PORTA, ROT, MODELOS = sys.argv[1], sys.argv[2], sys.argv[3].split(",")
EXTRA = json.loads(sys.argv[4]) if len(sys.argv) > 4 else {}
URL = f"http://127.0.0.1:{PORTA}"
PERSONA = ("Voce e a Astolfo, uma assistente virtual animada que canta, toca instrumentos e joga com o usuario. "
           "Responda em portugues do Brasil, em no maximo duas frases curtas.")
PERG = ["Oi! Tudo bem? O que voce gosta de fazer?", "Estou perdendo nessa fase, alguma dica rapida?"]

def servidores():
    return [p for p in psutil.process_iter(["name", "cmdline"]) if (p.info["name"] or "").lower() == "llama-server.exe"]

for m in MODELOS:
    requests.post(f"{URL}/api/generate", json={"model": m, "keep_alive": 0}); time.sleep(3)
    antes = {p.pid for p in servidores()}
    opts = {"num_gpu": 0, "num_thread": 8, "num_ctx": 4096, "num_predict": 60, **EXTRA}
    ger, txt = [], ""
    for q in PERG:
        d = requests.post(f"{URL}/api/chat", json={"model": m, "stream": False, "think": False, "keep_alive": "5m",
            "messages": [{"role": "system", "content": PERSONA}, {"role": "user", "content": q}], "options": opts}, timeout=600).json()
        ger.append(d["eval_count"] / (d["eval_duration"] / 1e9)); txt = txt or d["message"]["content"][:160]
    novos = [p for p in servidores() if p.pid not in antes] or servidores()
    p = max(novos, key=lambda x: x.memory_info().rss)
    i = p.memory_full_info(); cmd = " ".join(p.cmdline())
    flags = {k: (cmd.split(k)[1].split()[0] if k in cmd else None) for k in ("--load-mode", "-c", "--cache-type-k", "--flash-attn")}
    reg = {"rotulo": ROT, "modelo": m, "opcoes": EXTRA, "privada_mb": round(i.private / 2**20), "working_set_mb": round(i.rss / 2**20),
           "geracao_tok_s": round(st.median(ger), 1), "flags_llama_server": flags, "amostra": txt,
           "ram_livre_sistema_mb": round(psutil.virtual_memory().available / 2**20)}
    print(json.dumps(reg, ensure_ascii=False))
    with open(B / "resultados" / "ram_llm.jsonl", "a", encoding="utf-8") as f: f.write(json.dumps(reg, ensure_ascii=False) + "\n")
    requests.post(f"{URL}/api/generate", json={"model": m, "keep_alive": 0}); time.sleep(2)
