# ! Alteração de IA - Revisar: arquivo novo inteiro.
# ! Motivo: abrir qualquer modelo da IA (RVC, visão, voz) no Netron para ver as camadas
# e conexões da rede neural no navegador, tudo local.
"""Mostra a rede neural de um modelo no navegador, usando o Netron.

Uso:
    python tools/ver_rede.py caminho/do/modelo.onnx
    python tools/ver_rede.py caminho/do/modelo.pth --porta 8081

Formatos que desenham o grafo completo: .onnx, .tflite, .keras, .h5, TorchScript (.pt).
Um .pth comum (como o modelo RVC do Applio) guarda só os pesos: o Netron lista as
camadas e o tamanho de cada uma, mas não as ligações. Para ver o grafo, exporte para ONNX.
"""

import argparse
import sys
from pathlib import Path

try:
    import netron
except ImportError:
    sys.exit("Netron não instalado. Rode: pip install -r requirements-ferramentas.txt")


def main():
    parser = argparse.ArgumentParser(description="Abre um modelo no Netron.")
    parser.add_argument("modelo", type=Path, help="arquivo do modelo")
    parser.add_argument("--porta", type=int, default=8080, help="porta local (padrão 8080)")
    args = parser.parse_args()

    if not args.modelo.is_file():
        sys.exit(f"Arquivo não encontrado: {args.modelo}")

    print(f"Abrindo {args.modelo.name} em http://localhost:{args.porta} (Ctrl+C para sair)")
    netron.start(str(args.modelo), address=("localhost", args.porta), browse=True)
    try:
        netron.wait()
    except KeyboardInterrupt:
        netron.stop()


if __name__ == "__main__":
    main()
