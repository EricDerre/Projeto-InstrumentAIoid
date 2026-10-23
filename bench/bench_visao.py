"""Benchmark de visao: captura de tela (dxcam) + YOLO26n em CPU (ONNX), DirectML (iGPU/dGPU) e CUDA.
Uso: python bench_visao.py [rotulo_cenario] -> resultados/visao_<rotulo>.jsonl
"""
import json, sys, time, pathlib, statistics as st
import numpy as np

CENARIO = sys.argv[1] if len(sys.argv) > 1 else "sem_jogo"
B = pathlib.Path(__file__).resolve().parent; M = B / "modelos"; R = B / "resultados"
M.mkdir(exist_ok=True); R.mkdir(exist_ok=True)
N = 60
def grava(reg):
    print(json.dumps(reg, ensure_ascii=False))
    with open(R / f"visao_{CENARIO}.jsonl", "a", encoding="utf-8") as f: f.write(json.dumps(reg, ensure_ascii=False) + "\n")

# 1. captura
import dxcam
cam = dxcam.create(output_color="BGR")
quadro = None; ts = []
# video_mode=True repete o ultimo quadro quando a tela nao muda (desktop parado nao gera quadros novos)
cam.start(target_fps=120, video_mode=True); time.sleep(0.5)
t0 = time.time(); n = 0
while time.time() - t0 < 3:
    t = time.time(); f = cam.get_latest_frame(); ts.append(time.time() - t); n += 1
    if f is not None: quadro = f
fps = n / (time.time() - t0); cam.stop()
grava({"cenario": CENARIO, "peca": "captura_dxcam_1080p", "ms_por_quadro_mediana": round(st.median(ts) * 1000, 2) if ts else None, "quadros_por_s_obtidos": round(fps, 1), "alvo_fps": 120})
if quadro is None: quadro = (np.random.rand(1080, 1920, 3) * 255).astype(np.uint8)
del cam

# 2. YOLO26n
import cv2, onnxruntime as ort
from ultralytics import YOLO
pt = M / "yolo26n.pt"
modelo = YOLO("yolo26n.pt") if not pt.exists() else YOLO(str(pt))
for tam in (320, 640):
    onx = M / f"yolo26n_{tam}.onnx"
    if not onx.exists():
        caminho = modelo.export(format="onnx", imgsz=tam, simplify=True); pathlib.Path(caminho).replace(onx)
    img = cv2.resize(quadro, (tam, tam))[:, :, ::-1].transpose(2, 0, 1)[None].astype(np.float32) / 255
    cfgs = [("cpu_onnx", ["CPUExecutionProvider"], {})]
    for dev in (0, 1):
        cfgs.append((f"directml_dev{dev}", [("DmlExecutionProvider", {"device_id": dev}), "CPUExecutionProvider"], {}))
    for nome, prov, _ in cfgs:
        try:
            so = ort.SessionOptions()
            if nome.startswith("directml"): so.enable_mem_pattern = False; so.execution_mode = ort.ExecutionMode.ORT_SEQUENTIAL
            s = ort.InferenceSession(str(onx), so, providers=prov)
            ent = s.get_inputs()[0].name
            for _ in range(5): s.run(None, {ent: img})
            tt = []
            for _ in range(N):
                t = time.time(); s.run(None, {ent: img}); tt.append(time.time() - t)
            grava({"cenario": CENARIO, "peca": f"yolo26n_{tam}", "backend": nome, "providers_ativos": s.get_providers()[:1],
                   "ms_mediana": round(st.median(tt) * 1000, 2), "ms_p90": round(sorted(tt)[int(N * .9)] * 1000, 2)})
        except Exception as e:
            grava({"cenario": CENARIO, "peca": f"yolo26n_{tam}", "backend": nome, "erro": str(e)[:200]})
    # CUDA via PyTorch (FP32, a GTX 16 nao gosta de FP16)
    try:
        import torch
        if torch.cuda.is_available():
            fr = cv2.resize(quadro, (tam, tam))
            for _ in range(5): modelo.predict(fr, imgsz=tam, device=0, half=False, verbose=False)
            tt = []
            for _ in range(N):
                t = time.time(); modelo.predict(fr, imgsz=tam, device=0, half=False, verbose=False); torch.cuda.synchronize(); tt.append(time.time() - t)
            grava({"cenario": CENARIO, "peca": f"yolo26n_{tam}", "backend": "cuda_torch_fp32", "gpu": torch.cuda.get_device_name(0),
                   "ms_mediana": round(st.median(tt) * 1000, 2), "ms_p90": round(sorted(tt)[int(N * .9)] * 1000, 2),
                   "vram_reservada_mb": round(torch.cuda.memory_reserved() / 2**20)})
    except Exception as e:
        grava({"cenario": CENARIO, "peca": f"yolo26n_{tam}", "backend": "cuda_torch_fp32", "erro": str(e)[:200]})
