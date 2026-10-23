"""Benchmark do RVC (motor do Applio) com o modelo astolfoV3 do Eric.
Rodar com o Python do venv do Applio, de dentro da pasta applio:
  ..\applio\.venv\Scripts\python.exe ..\bench_rvc.py <cpu|gpu> [rotulo_cenario]
"""
import os, sys
DISP = sys.argv[1] if len(sys.argv) > 1 else "gpu"
CENARIO = sys.argv[2] if len(sys.argv) > 2 else "sem_jogo"
import json, time, pathlib, statistics as st, subprocess
import soundfile as sf

B = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(B / "applio")); os.chdir(B / "applio")
import torch
if DISP == "cpu":
    torch.cuda.is_available = lambda: False  # forca o Applio a escolher CPU
from rvc.infer.infer import VoiceConverter
import core, torch

ENTRADA = B / "audio" / "kokoro_pf_dora.wav"
PTH = B / "modelos" / "rvc" / "astolfoV3_300e_7800s.pth"
IDX = B / "modelos" / "rvc" / "astolfoV3.index"
dur = sf.info(ENTRADA).duration

def vram_mb():
    try:
        r = subprocess.run(["nvidia-smi", "--query-gpu=memory.used", "--format=csv,noheader,nounits"], capture_output=True, text=True)
        return int(r.stdout.strip())
    except Exception:
        return None

vc = VoiceConverter()
for f0 in ("rmvpe", "fcpe"):
    v0 = vram_mb(); tempos = []
    for i in range(3):
        saida = B / "audio" / f"rvc_{DISP}_{f0}_{i}.wav"
        kw = core._base_infer_kwargs(f0_method=f0, pth_path=str(PTH), index_path=str(IDX), pitch=0)
        kw["audio_input_path"] = str(ENTRADA); kw["audio_output_path"] = str(saida)
        t = time.time(); vc.convert_audio(**kw); tempos.append(time.time() - t)
    reg = {"cenario": CENARIO, "peca": "rvc_astolfoV3", "dispositivo": DISP, "f0": f0,
           "cuda": torch.cuda.is_available(), "audio_s": round(dur, 2),
           "primeira_s": round(tempos[0], 2), "quente_s_mediana": round(st.median(tempos[1:]), 2),
           "rtf_quente": round(st.median(tempos[1:]) / dur, 3),
           "vram_pico_torch_mb": round(torch.cuda.max_memory_allocated() / 2**20) if torch.cuda.is_available() else 0,
           "vram_delta_nvsmi_mb": (vram_mb() - v0) if v0 is not None else None}
    print(json.dumps(reg, ensure_ascii=False))
    with open(B / "resultados" / f"rvc_{CENARIO}.jsonl", "a", encoding="utf-8") as fh:
        fh.write(json.dumps(reg, ensure_ascii=False) + "\n")
