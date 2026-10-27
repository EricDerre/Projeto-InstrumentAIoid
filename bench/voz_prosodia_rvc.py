# ! Alteração de IA - Revisar
r"""Teste de entonação da SennAI: RVC astolfoV3 com a curva de pitch (F0) moldada por tipo de frase.

O RVC copia a curva de pitch da entrada: se o TTS fala "Preparado?" descendo, a SennAI também desce.
Aqui a curva é corrigida DENTRO do RVC (gancho em Pipeline.get_f0), antes da síntese, então não há
artefato de PSOLA: o RVC sintetiza direto na curva nova. Rodar de dentro de bench com o venv do Applio:
  applio\.venv\Scripts\python.exe voz_prosodia_rvc.py
Entrada: audio/prosodia/tts/*.wav (gerados por voz_frases_tts.py)
Saída: audio/prosodia/<variante>.wav (frases emendadas) e resultados/prosodia_f0.npz (curvas p/ gráfico)
"""
import os, sys, json, time, pathlib
import numpy as np, soundfile as sf

B = pathlib.Path(__file__).resolve().parent
P = B / "audio" / "prosodia"; TTS = P / "tts"
sys.path.insert(0, str(B / "applio")); os.chdir(B / "applio")
from rvc.infer.infer import VoiceConverter
from rvc.infer.pipeline import Pipeline
import core

PTH = B / "modelos" / "rvc" / "astolfoV3_300e_7800s.pth"
IDX = B / "modelos" / "rvc" / "astolfoV3.index"
FRASES = json.loads((P / "frases.json").read_text(encoding="utf-8"))
QUADROS_S = 100  # o F0 do RVC tem 100 quadros por segundo (hop 160 a 16 kHz)


def suave(t):
    t = np.clip(t, 0, 1); return t * t * (3 - 2 * t)


def moldar(f0, pad, tipo=".", faixa=1.0, subida=7.0, curva_pergunta="sobe-desce"):
    """Muda a curva de pitch em semitons, em torno da mediana da frase.
    faixa: multiplica a distância de cada ponto até a mediana (1.0 = igual ao TTS; 1.4 = 40% mais melodia).
    tipo "?sn": sobe ~subida st na última palavra; "sobe-desce" = sobe na sílaba tônica e cai um pouco
    no fim (padrão do português do Brasil), "sobe" = sobe até o fim (mais "anime"/inglês)."""
    f = f0.copy(); v = f > 0
    idx = np.where(v)[0]; idx = idx[(idx >= pad) & (idx < len(f) - pad)]
    if len(idx) < 5:
        return f
    m = np.median(f[idx]); ini, fim = idx[0], idx[-1]
    if tipo == "!":
        faixa *= 1.2
    st = 12 * np.log2(np.where(v, f, m) / m) * faixa
    soma = np.zeros(len(f))
    if tipo == "!":
        soma[ini:fim + 1] += 1.5                       # exclamação: um pouco mais aguda e animada
    elif tipo in (".", "?qu"):
        a = max(ini, fim - int(0.30 * QUADROS_S))      # afirmação/pergunta com "qual": cai no final
        soma[a:fim + 1] += -2.0 * suave((np.arange(a, fim + 1) - a) / max(1, fim - a))
    elif tipo == "?sn":
        a = max(ini, fim - int(0.45 * QUADROS_S))      # ~última palavra
        t = (np.arange(a, fim + 1) - a) / max(1, fim - a)
        # a frase do TTS costuma cair no fim; primeiro desfaz essa queda (zera a tendência da janela)
        st[a:fim + 1] -= np.linspace(0, st[fim] - st[a], fim - a + 1) * v[a:fim + 1]
        if curva_pergunta == "sobe":
            c = subida * suave(t)
        else:
            pico = 0.6
            c = np.where(t < pico, subida * suave(t / pico), subida - (subida * 0.45) * suave((t - pico) / (1 - pico)))
        soma[a:fim + 1] += c
    f[v] = m * 2 ** ((st[v] + soma[v]) / 12)
    return f


FORMA = None; CURVAS = {}; ROTULO = None
_get_f0 = Pipeline.get_f0
def get_f0_moldado(self, x, p_len, *a, **kw):
    coarse, f0 = _get_f0(self, x, p_len, *a, **kw)
    antes = f0.copy()
    if FORMA is not None:
        f0 = moldar(f0, pad=self.t_pad // self.window, **FORMA)
        mel = 1127 * np.log(1 + f0 / 700)
        mel[mel > 0] = (mel[mel > 0] - self.f0_mel_min) * 254 / (self.f0_mel_max - self.f0_mel_min) + 1
        coarse = np.rint(np.clip(mel, 1, 255)).astype(int)
    CURVAS[ROTULO + "_antes"] = antes; CURVAS[ROTULO + "_depois"] = f0.copy()
    return coarse, f0
Pipeline.get_f0 = get_f0_moldado

# tom: o F0 do dataset de treino tem mediana ~429 Hz (amostra em bench/modelos/rvc/dataset_f0);
# o Kokoro pf_dora fala em ~175 Hz, ou seja ~15 semitons abaixo do que o modelo aprendeu.
TOM = int(sys.argv[1]) if len(sys.argv) > 1 else 12
VARIANTES = {
    # nome: (motor TTS, pitch, index_rate, protect, moldar?, faixa, curva da pergunta)
    "v0_atual":                ("kokoro", 0,   0.30, 0.33, False, 1.0, None),
    "v1a_tom8":                ("kokoro", 8,   0.30, 0.33, False, 1.0, None),
    "v1b_tom12":               ("kokoro", 12,  0.30, 0.33, False, 1.0, None),
    "v1c_tom15":               ("kokoro", 15,  0.30, 0.33, False, 1.0, None),
    "v2_tom_faixa":            ("kokoro", TOM, 0.30, 0.33, True,  1.4, "nenhuma"),
    "v3_tom_faixa_entonacao":  ("kokoro", TOM, 0.30, 0.33, True,  1.4, "sobe-desce"),
    "v4_entonacao_sobe":       ("kokoro", TOM, 0.30, 0.33, True,  1.4, "sobe"),
    "v5_v3_index060":          ("kokoro", TOM, 0.60, 0.33, True,  1.4, "sobe-desce"),
    "v6_v3_protect050":        ("kokoro", TOM, 0.30, 0.50, True,  1.4, "sobe-desce"),
    "v7_piper_entonacao":      ("piper",  TOM, 0.30, 0.33, True,  1.4, "sobe-desce"),
    "v8_xtts_tom12":           ("xtts",   TOM, 0.30, 0.33, False, 1.0, None),
    "v9_xtts_entonacao":       ("xtts",   TOM, 0.30, 0.33, True,  1.0, "sobe-desce"),
}
SO = sys.argv[2].split(",") if len(sys.argv) > 2 else None  # ex.: 12 v8_xtts_tom12,v9_xtts_entonacao
if SO: VARIANTES = {k: v for k, v in VARIANTES.items() if k in SO}
PAUSA = {".": 0.35, "!": 0.30, "?sn": 0.45, "?qu": 0.45}

vc = VoiceConverter(); tempos = {}
for nome, (motor, tom, idx_rate, prot, molda, faixa, curva) in VARIANTES.items():
    pedacos = []; t0 = time.time()
    for n, (texto, tipo) in enumerate(FRASES):
        if not molda:
            FORMA = None
        elif curva == "nenhuma":
            FORMA = dict(tipo="faixa", faixa=faixa)
        else:
            FORMA = dict(tipo=tipo, faixa=faixa, curva_pergunta=curva)
        ROTULO = f"{nome}_{n}"
        saida = P / f"_tmp_{nome}_{n}.wav"
        kw = core._base_infer_kwargs(f0_method="rmvpe", pth_path=str(PTH), index_path=str(IDX),
                                     pitch=tom, index_rate=idx_rate, protect=prot)
        kw["audio_input_path"] = str(TTS / f"{motor}_{n}.wav"); kw["audio_output_path"] = str(saida)
        vc.convert_audio(**kw)
        a, sr = sf.read(saida); os.remove(saida)
        pedacos += [a, np.zeros(int(PAUSA[tipo] * sr))]
    sf.write(P / f"{nome}.wav", np.concatenate(pedacos), sr)
    tempos[nome] = round(time.time() - t0, 2); print(nome, tempos[nome], "s")
np.savez(B / "resultados" / ("prosodia_f0.npz" if not SO else "prosodia_f0_" + "_".join(SO) + ".npz"), **CURVAS)
if not SO: (B / "resultados" / "prosodia_tempos.json").write_text(json.dumps({"tom": TOM, "tempos_s": tempos}, indent=1))
