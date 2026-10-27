# ! Alteração de IA - Revisar
r"""Gera as frases de teste de entonação da SennAI, uma frase por arquivo.
Rodar com o venv principal do bench:  .venv\Scripts\python.exe voz_frases_tts.py
Saída: audio/prosodia/tts/<motor>_<n>.wav  e  audio/prosodia/frases.json
"""
import json, pathlib, wave
import soundfile as sf

B = pathlib.Path(__file__).resolve().parent; M = B / "modelos"
SAIDA = B / "audio" / "prosodia" / "tts"; SAIDA.mkdir(parents=True, exist_ok=True)

# Uma frase por item: no pipeline real o texto do LLM também é quebrado por frase (streaming).
# Tipo da frase decide a curva de entonação no RVC: "." afirmação, "!" exclamação,
# "?sn" pergunta de sim/não (sobe no fim), "?qu" pergunta com que/qual/quem... (cai no fim, como no português falado).
FRASES = [
    ("Oi!", "!"),
    ("Eu sou a Sennái.", "."),
    ("Hoje a gente vai jogar um pouquinho e depois, quem sabe, tocar uma música juntos.", "."),
    ("Preparado?", "?sn"),
    ("Você quer jogar agora?", "?sn"),
    ("Qual jogo você quer jogar?", "?qu"),
    ("Nossa, que jogada incrível!", "!"),
]
(B / "audio" / "prosodia" / "frases.json").write_text(json.dumps(FRASES, ensure_ascii=False, indent=1), encoding="utf-8")

import os; os.environ.setdefault("ONNX_PROVIDER", "CPUExecutionProvider")  # no DirectML o Kokoro quebra
from kokoro_onnx import Kokoro
k = Kokoro(str(M / "kokoro-v1.0.onnx"), str(M / "voices-v1.0.bin"))
from piper import PiperVoice
pv = PiperVoice.load(str(M / "pt_BR-faber-medium.onnx"))

for n, (texto, _) in enumerate(FRASES):
    amostras, sr = k.create(texto, voice="pf_dora", speed=1.0, lang="pt-br")
    sf.write(SAIDA / f"kokoro_{n}.wav", amostras, sr)
    with wave.open(str(SAIDA / f"piper_{n}.wav"), "wb") as w:
        pv.synthesize_wav(texto, w)
    print("ok", n, texto)
