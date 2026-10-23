# ! Alteração de IA - Revisar: arquivo novo inteiro.
# ! Motivo: o .pth do RVC só guarda pesos; exportando para ONNX dá para ver o grafo
# completo (camadas e ligações) no Netron com tools/ver_rede.py. Roda só na CPU.
"""Exporta um modelo de voz RVC (.pth do Applio) para ONNX.

Uso (com o Python do Applio, que já tem torch):
    bench\\applio\\.venv\\Scripts\\python.exe tools/exportar_onnx_rvc.py bench/modelos/rvc/voz.pth
    ... --saida models/voz.onnx --opset 18 --sem-ruido

Entradas do ONNX: phone (1, N, 768 no v2 / 256 no v1), phone_lengths (1,),
pitch (1, N) inteiro, pitchf (1, N), sid (1,). N é dinâmico.
Saída: audio (1, 1, amostras).
"""

import argparse
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
APPLIO = RAIZ / "bench" / "applio"

try:
    import torch
except ImportError:
    sys.exit("torch não instalado. Use o Python do Applio: bench\\applio\\.venv\\Scripts\\python.exe")


class Envoltorio(torch.nn.Module):
    """Chama o infer do sintetizador e devolve só o áudio."""

    def __init__(self, rede, sem_ruido=False):
        super().__init__()
        self.rede = rede
        self.sem_ruido = sem_ruido

    def forward(self, phone, phone_lengths, pitch, pitchf, sid):
        if not self.sem_ruido:
            return self.rede.infer(phone, phone_lengths, pitch, pitchf, sid)[0]
        # Mesmo caminho do infer_latent do Applio, mas sem o torch.randn_like
        # (algumas versões do exportador não aceitam ruído aleatório).
        r = self.rede
        g = r.emb_g(sid).unsqueeze(-1)
        m_p, logs_p, x_mask = r.enc_p(phone, pitch, phone_lengths)
        z = r.flow(m_p * x_mask, x_mask, g=g, reverse=True)
        return r.dec(z * x_mask, pitchf, g=g)


def montar_sintetizador(ckpt):
    """Monta o Synthesizer do Applio do mesmo jeito que rvc/infer/infer.py faz."""
    sys.path.insert(0, str(APPLIO))
    from rvc.lib.algorithm.synthesizers import Synthesizer

    config = list(ckpt["config"])
    config[-3] = ckpt["weight"]["emb_g.weight"].shape[0]  # número de vozes
    versao = ckpt.get("version", "v1")
    rede = Synthesizer(
        *config,
        use_f0=ckpt.get("f0", 1),
        text_enc_hidden_dim=768 if versao == "v2" else 256,
        vocoder=ckpt.get("vocoder", "HiFi-GAN"),
    )
    rede.load_state_dict(ckpt["weight"], strict=False)
    rede.remove_weight_norm()  # o remove_weight_norm do Applio ainda usa o enc_q
    del rede.enc_q  # só serve no treino
    fixar_layer_norm(rede)
    return rede.float().eval(), versao


def fixar_layer_norm(rede):
    """Troca o forward dos LayerNorm do Applio por um com o número de canais fixo.

    O original passa `x.size(-1)` para o layer_norm, e o exportador clássico do
    ONNX não aceita esse tamanho calculado na hora. A conta é a mesma.
    """
    from rvc.lib.algorithm.normalization import LayerNorm

    def forward_fixo(modulo, canais):
        def forward(x):
            x = x.transpose(1, -1)
            x = torch.nn.functional.layer_norm(x, (canais,), modulo.gamma, modulo.beta, modulo.eps)
            return x.transpose(1, -1)
        return forward

    for modulo in rede.modules():
        if isinstance(modulo, LayerNorm):
            modulo.forward = forward_fixo(modulo, int(modulo.gamma.shape[0]))


def main():
    parser = argparse.ArgumentParser(description="Exporta um modelo RVC (.pth) para ONNX.")
    parser.add_argument("modelo", type=Path, help="arquivo .pth do modelo de voz")
    parser.add_argument("--saida", type=Path, help="padrão: models/<nome>.onnx")
    parser.add_argument("--opset", type=int, default=17)
    parser.add_argument("--sem-ruido", action="store_true", help="tira o ruído aleatório do grafo")
    args = parser.parse_args()

    if not args.modelo.is_file():
        sys.exit(f"Arquivo não encontrado: {args.modelo}")
    saida = args.saida or RAIZ / "models" / f"{args.modelo.stem}.onnx"
    saida.parent.mkdir(parents=True, exist_ok=True)

    ckpt = torch.load(args.modelo, map_location="cpu", weights_only=False)
    if not ckpt.get("f0", 1):
        sys.exit("Modelo sem f0 (pitch): este exportador só cobre modelos com pitch.")
    rede, versao = montar_sintetizador(ckpt)
    print(f"Modelo {versao}, {ckpt['config'][-1]} Hz, vocoder {ckpt.get('vocoder', 'HiFi-GAN')}")

    n = 200
    dim = 768 if versao == "v2" else 256
    exemplo = (
        torch.randn(1, n, dim),
        torch.tensor([n], dtype=torch.long),
        torch.randint(1, 255, (1, n), dtype=torch.long),
        torch.rand(1, n) * 400 + 50,
        torch.tensor([0], dtype=torch.long),
    )
    nomes = ["phone", "phone_lengths", "pitch", "pitchf", "sid"]
    eixos = {
        "phone": {1: "quadros"},
        "pitch": {1: "quadros"},
        "pitchf": {1: "quadros"},
        "audio": {2: "amostras"},
    }

    with torch.no_grad():
        torch.onnx.export(
            Envoltorio(rede, args.sem_ruido),
            exemplo,
            str(saida),
            input_names=nomes,
            output_names=["audio"],
            dynamic_axes=eixos,
            opset_version=args.opset,
            do_constant_folding=True,
            dynamo=False,  # exportador clássico: não precisa do onnxscript
        )
    print(f"Salvo em {saida} ({saida.stat().st_size / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
