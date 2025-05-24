import requests
import json

OLLAMA_API_URL = "http://localhost:11434/api/generate"

def stream_resposta_do_ollama(mensagem_usuario: str):
    payload = {
        "model": "mistral",
        "prompt": mensagem_usuario,
        "stream": True
    }

    resposta = requests.post(OLLAMA_API_URL, json=payload, stream=True)

    for linha in resposta.iter_lines():
        if linha:
            try:
                data = linha.decode("utf-8")
                parte = json.loads(data)  # cada linha é um JSON: {"response": "texto"}
                yield parte["response"]
            except Exception as e:
                yield f"[Erro de parsing: {str(e)}]"
