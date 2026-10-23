import requests
import json
import time

# ! Alteração de IA - Revisar: import do barramento de eventos.
# ! Motivo: avisar o painel /cerebro quando o modelo é chamado e quando termina.
from app.cerebro import emitir

OLLAMA_API_URL = "http://localhost:11434/api/generate"

def stream_resposta_do_ollama(mensagem_usuario: str):
    payload = {
        "model": "mistral",
        "prompt": mensagem_usuario,
        "stream": True
    }

    # ! Alteração de IA - Revisar: eventos de início, fim e erro da chamada ao Ollama.
    # ! Motivo: o painel mostra a seta central -> llm acendendo, e quanto tempo e tokens a resposta levou.
    inicio = time.time()
    tokens = 0
    emitir("central", "llm", "pedido", mensagem_usuario[:80], modelo=payload["model"])

    resposta = requests.post(OLLAMA_API_URL, json=payload, stream=True)

    for linha in resposta.iter_lines():
        if linha:
            try:
                data = linha.decode("utf-8")
                parte = json.loads(data)  # cada linha é um JSON: {"response": "texto"}
                tokens += 1
                if parte.get("done"):
                    tokens = parte.get("eval_count", tokens - 1)  # o Ollama manda a contagem real no fim
                    segundos = time.time() - inicio
                    emitir("llm", "central", "resposta", f"{tokens} tokens em {segundos:.1f} s",
                           tokens=tokens, segundos=round(segundos, 2))
                yield parte["response"]
            except Exception as e:
                emitir("llm", "central", "erro", f"parsing: {e}")
                yield f"[Erro de parsing: {str(e)}]"
