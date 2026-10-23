"""Mede quanto de RAM cada modulo ocupa depois de carregado (privada x working set).
Uso: python bench_ram.py [llm|voz|visao|tudo]  -> resultados/ram.jsonl
Privada = memoria que so aquele processo usa (o que realmente disputa os 16 GB).
Working set = o que esta na RAM agora, incluindo arquivos mapeados (pesos com mmap), que o Windows pode descartar.
"""
import json, os, sys, time, pathlib, subprocess
import psutil, requests

B = pathlib.Path(__file__).resolve().parent; R = B / "resultados"; R.mkdir(exist_ok=True)
QUAL = sys.argv[1] if len(sys.argv) > 1 else "tudo"
URL = "http://localhost:11434"

def mb(x): return round(x / 2**20)
def livre_mb(): return mb(psutil.virtual_memory().available)

def mem(p):
    i = p.memory_full_info()
    return {"privada_mb": mb(getattr(i, "private", i.uss)), "working_set_mb": mb(i.rss)}

def grava(reg):
    reg["ram_livre_sistema_mb"] = livre_mb()
    print(json.dumps(reg, ensure_ascii=False))
    with open(R / "ram.jsonl", "a", encoding="utf-8") as f: f.write(json.dumps(reg, ensure_ascii=False) + "\n")

def runners():
    out = []
    for p in psutil.process_iter(["name", "cmdline"]):
        try:
            if p.info["name"] and p.info["name"].lower().startswith("ollama") and "runner" in " ".join(p.info["cmdline"] or []):
                out.append(p)
        except Exception: pass
    return out

def llm(modelo, opts, rot):
    requests.post(f"{URL}/api/generate", json={"model": modelo, "keep_alive": 0}); time.sleep(3)
    antes = livre_mb()
    requests.post(f"{URL}/api/chat", json={"model": modelo, "stream": False, "keep_alive": "5m", "think": False,
        "messages": [{"role": "user", "content": "Diga ola em uma palavra."}],
        "options": {"num_predict": 5, **opts}}, timeout=600)
    time.sleep(2)
    soma = {"privada_mb": 0, "working_set_mb": 0}
    for p in runners():
        m = mem(p); soma = {k: soma[k] + m[k] for k in soma}
    grava({"peca": f"llm {modelo}", "config": rot, **soma, "queda_ram_livre_mb": antes - livre_mb()})
    requests.post(f"{URL}/api/generate", json={"model": modelo, "keep_alive": 0}); time.sleep(3)

if QUAL in ("llm", "tudo"):
    for m in ("qwen3:1.7b", "llama3.2:3b", "qwen3:4b-instruct"):
        llm(m, {"num_gpu": 0, "num_ctx": 4096}, "cpu ctx4096")
        llm(m, {"num_gpu": 0, "num_ctx": 2048}, "cpu ctx2048")
        llm(m, {"num_gpu": 0, "num_ctx": 4096, "use_mmap": False}, "cpu ctx4096 sem mmap")

eu = psutil.Process(os.getpid())
if QUAL in ("voz", "tudo"):
    os.environ["ONNX_PROVIDER"] = "CPUExecutionProvider"
    base = mem(eu)
    from piper import PiperVoice
    pv = PiperVoice.load(str(B / "modelos" / "pt_BR-faber-medium.onnx")); m = mem(eu)
    grava({"peca": "tts piper faber", **{k: m[k] - base[k] for k in m}}); base = m
    from kokoro_onnx import Kokoro
    k = Kokoro(str(B / "modelos" / "kokoro-v1.0.onnx"), str(B / "modelos" / "voices-v1.0.bin"))
    k.create("Ola, tudo bem?", voice="pf_dora", lang="pt-br"); m = mem(eu)
    grava({"peca": "tts kokoro", **{k2: m[k2] - base[k2] for k2 in m}}); base = m
    from faster_whisper import WhisperModel
    for tam in ("base", "small"):
        w = WhisperModel(tam, device="cpu", compute_type="int8", download_root=str(B / "modelos" / "whisper"))
        list(w.transcribe(str(B / "audio" / "kokoro_pf_dora.wav"), language="pt")[0]); m = mem(eu)
        grava({"peca": f"stt whisper {tam} int8", **{k2: m[k2] - base[k2] for k2 in m}}); base = m
        del w

if QUAL in ("visao", "tudo"):
    import numpy as np, onnxruntime as ort
    base = mem(eu)
    s = ort.InferenceSession(str(B / "modelos" / "yolo26n_320.onnx"), providers=[("DmlExecutionProvider", {"device_id": 0})])
    s.run(None, {s.get_inputs()[0].name: np.zeros((1, 3, 320, 320), np.float32)}); m = mem(eu)
    grava({"peca": "yolo26n 320 directml radeon", **{k2: m[k2] - base[k2] for k2 in m}})
