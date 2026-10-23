"""Benchmark de TTS (Kokoro, Piper) e STT (faster-whisper) em CPU.
Uso: python bench_voz.py [rotulo_cenario]  -> resultados/voz_<rotulo>.jsonl e audios em audio/
"""
import json, sys, time, pathlib, urllib.request, wave
import numpy as np, soundfile as sf

CENARIO = sys.argv[1] if len(sys.argv) > 1 else "sem_jogo"
B = pathlib.Path(__file__).resolve().parent; M = B / "modelos"; A = B / "audio"; R = B / "resultados"
for p in (M, A, R): p.mkdir(exist_ok=True)
TEXTO = ("Oi! Eu sou a Astolfo. Hoje a gente vai jogar um pouquinho e depois, quem sabe, "
         "tocar uma musica juntos. Preparado?")
BAIXAR = {
    "kokoro-v1.0.onnx": "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx",
    "voices-v1.0.bin": "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin",
    "pt_BR-faber-medium.onnx": "https://huggingface.co/rhasspy/piper-voices/resolve/main/pt/pt_BR/faber/medium/pt_BR-faber-medium.onnx",
    "pt_BR-faber-medium.onnx.json": "https://huggingface.co/rhasspy/piper-voices/resolve/main/pt/pt_BR/faber/medium/pt_BR-faber-medium.onnx.json",
}
for nome, url in BAIXAR.items():
    if not (M / nome).exists():
        print("baixando", nome); urllib.request.urlretrieve(url, M / nome)

res = []
def grava(reg):
    print(json.dumps(reg, ensure_ascii=False)); res.append(reg)
    with open(R / f"voz_{CENARIO}.jsonl", "a", encoding="utf-8") as f: f.write(json.dumps(reg, ensure_ascii=False) + "\n")

# Kokoro
from kokoro_onnx import Kokoro
k = Kokoro(str(M / "kokoro-v1.0.onnx"), str(M / "voices-v1.0.bin"))
k.create("Ola.", voice="pf_dora", speed=1.0, lang="pt-br")  # aquecimento
for voz in ("pf_dora", "pm_alex"):
    t = time.time(); amostras, sr = k.create(TEXTO, voice=voz, speed=1.0, lang="pt-br"); dt = time.time() - t
    dur = len(amostras) / sr; sf.write(A / f"kokoro_{voz}.wav", amostras, sr)
    grava({"cenario": CENARIO, "peca": "tts_kokoro", "voz": voz, "audio_s": round(dur, 2), "tempo_s": round(dt, 2), "rtf": round(dt / dur, 3)})

# Piper
from piper import PiperVoice
pv = PiperVoice.load(str(M / "pt_BR-faber-medium.onnx"))
def piper_wav(caminho):
    with wave.open(str(caminho), "wb") as w: pv.synthesize_wav(TEXTO, w)
piper_wav(A / "piper_aquec.wav")
t = time.time(); piper_wav(A / "piper_faber.wav"); dt = time.time() - t
dur = sf.info(A / "piper_faber.wav").duration
grava({"cenario": CENARIO, "peca": "tts_piper", "voz": "faber", "audio_s": round(dur, 2), "tempo_s": round(dt, 2), "rtf": round(dt / dur, 3)})

# STT
from faster_whisper import WhisperModel
for tam in ("base", "small"):
    wm = WhisperModel(tam, device="cpu", compute_type="int8", cpu_threads=8, download_root=str(M / "whisper"))
    list(wm.transcribe(str(A / "kokoro_pf_dora.wav"), language="pt")[0])  # aquecimento
    t = time.time(); segs, _ = wm.transcribe(str(A / "kokoro_pf_dora.wav"), language="pt", beam_size=1, vad_filter=True)
    texto = " ".join(s.text for s in segs).strip(); dt = time.time() - t
    dur = sf.info(A / "kokoro_pf_dora.wav").duration
    grava({"cenario": CENARIO, "peca": f"stt_whisper_{tam}_int8", "audio_s": round(dur, 2), "tempo_s": round(dt, 2), "rtf": round(dt / dur, 3), "texto": texto})
