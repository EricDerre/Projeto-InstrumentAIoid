import requests
import json
from app.persona import DESCRICAO

OLLAMA_API_URL = "http://localhost:11434/api/generate"

def carregar_descricao():
    return DESCRICAO.strip()

memoria_conversa = []

def atualizar_memoria(usuario: str, ia: str):
    # Adiciona o novo par de mensagens
    memoria_conversa.append({"role": "user", "content": usuario})
    memoria_conversa.append({"role": "ia", "content": ia})

    # Mantém só os últimos 6 elementos (3 pares)
    while len(memoria_conversa) > 6:
        memoria_conversa.pop(0)


def stream_resposta_do_ollama(mensagem_usuario: str):
    prompt_base = carregar_descricao()

    # Montar histórico textual da memória RAM
    historico = ""
    for msg in memoria_conversa:
        if msg["role"] == "user":
            historico += f"Usuário: {msg['content']}\n"
        elif msg["role"] == "ia":
            historico += f"Sena: {msg['content']}\n"

    # Montar o prompt final (alma + histórico + nova pergunta)
    prompt_final = (
        f"{prompt_base}\n\n"
        f"{historico}"
        f"Usuário: {mensagem_usuario}\n"
        f"Sena:"
    )

    payload = {
        "model": "mistral",
        "prompt": prompt_final,
        "stream": True
    }

    resposta = requests.post(OLLAMA_API_URL, json=payload, stream=True)

    resposta_ia = ""
    for linha in resposta.iter_lines():
        if linha:
            try:
                data = json.loads(linha.decode("utf-8"))
                parte = data["response"]
                resposta_ia += parte
                yield parte
            except Exception as e:
                yield f"[Erro de parsing: {str(e)}]"

    # Atualiza a memória após a resposta completa
    atualizar_memoria(mensagem_usuario, resposta_ia.strip())
