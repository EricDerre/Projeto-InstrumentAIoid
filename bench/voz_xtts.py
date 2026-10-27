# ! Alteração de IA - Revisar
r"""Gera as mesmas frases de teste com o XTTS-v2 (TTS mais expressivo, roda local na GTX 1650).
Venv próprio: bench\.venv-xtts (coqui-tts). Modelo (~1,9 GB) fica em bench\modelos\xtts.
Licença do XTTS-v2: Coqui Public Model License, só uso NÃO comercial (ok para o TCC).
  .venv-xtts\Scripts\python.exe voz_xtts.py
Saída: audio/prosodia/tts/xtts_<n>.wav e resultados/xtts_tempos.json
"""
import os, json, time, pathlib
B = pathlib.Path(__file__).resolve().parent
os.environ.setdefault("TTS_HOME", str(B / "modelos" / "xtts"))
os.environ.setdefault("COQUI_TOS_AGREED", "1")
import torch
from TTS.api import TTS

P = B / "audio" / "prosodia"; FRASES = json.loads((P / "frases.json").read_text(encoding="utf-8"))
FALANTE = "Ana Florence"
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to("cuda" if torch.cuda.is_available() else "cpu")
tts.tts("Olá.", speaker=FALANTE, language="pt")  # aquecimento
reg = []
for n, (texto, _) in enumerate(FRASES):
    t = time.time(); wav = tts.tts(texto.replace("Sennái", "Senái"), speaker=FALANTE, language="pt"); dt = time.time() - t
    sr = tts.synthesizer.output_sample_rate
    import soundfile as sf; sf.write(P / "tts" / f"xtts_{n}.wav", wav, sr)
    reg.append({"frase": n, "audio_s": round(len(wav) / sr, 2), "tempo_s": round(dt, 2), "rtf": round(dt / (len(wav) / sr), 3)})
    print(reg[-1])
reg.append({"vram_pico_mb": round(torch.cuda.max_memory_allocated() / 2**20) if torch.cuda.is_available() else 0})
(B / "resultados" / "xtts_tempos.json").write_text(json.dumps(reg, indent=1))
