"""RAM do processo do RVC (Applio) carregado na GPU. Rodar com applio\\.venv\\Scripts\\python.exe bench_ram_rvc.py"""
import json, os, sys, pathlib, psutil
B = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(B / "applio")); os.chdir(B / "applio")
eu = psutil.Process()
def m(): i = eu.memory_full_info(); return {"privada_mb": round(i.private / 2**20), "working_set_mb": round(i.rss / 2**20)}
base = m()
import torch, core
from rvc.infer.infer import VoiceConverter
imp = m()
vc = VoiceConverter()
kw = core._base_infer_kwargs(f0_method="fcpe", pth_path=str(B / "modelos/rvc/astolfoV3_300e_7800s.pth"), index_path=str(B / "modelos/rvc/astolfoV3.index"), inference_engine=(sys.argv[1] if len(sys.argv) > 1 else None))
kw["audio_input_path"] = str(B / "audio/kokoro_pf_dora.wav"); kw["audio_output_path"] = str(B / "audio/rvc_ram_teste.wav")
import time
vc.convert_audio(**kw); t = time.time(); vc.convert_audio(**kw); quente = round(time.time() - t, 2)
fim = m()
reg = {"peca": "rvc astolfoV3 gpu (processo inteiro)", "motor": (sys.argv[1] if len(sys.argv) > 1 else "torch"), "quente_s": quente, "so_python": base, "depois_imports_torch": imp, "carregado_e_convertido": fim,
       "ram_livre_sistema_mb": round(psutil.virtual_memory().available / 2**20)}
print(json.dumps(reg))
open(B / "resultados/ram.jsonl", "a", encoding="utf-8").write(json.dumps(reg) + "\n")
