import requests
import subprocess
import threading
import time
import os
import sys

# Inicia o Ollama com o modelo Mistral em segundo plano
def iniciar_ollama():
    print("Iniciando Ollama com o modelo Mistral...")
    subprocess.Popen(["ollama", "run", "mistral"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Inicia o servidor FastAPI (uvicorn)
def iniciar_api():
    print("Iniciando API FastAPI...")
    subprocess.Popen(["uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "8000", "--reload"], stdout=subprocess.DEVNULL)

# Espera a API iniciar
def aguardar_api():
    print("Aguardando API responder...")
    for _ in range(10):
        try:
            r = requests.get("http://127.0.0.1:8000/docs")
            if r.status_code == 200:
                print("API iniciada com sucesso.")
                return True
        except:
            time.sleep(1)
    return False

# Interface de terminal
def chat_terminal():
    print("\n=== InstrumentAIoid ===")
    print("Digite 'sair' para encerrar.\n")
    while True:
        msg = input("> Você: ")
        if msg.lower() == "sair":
            os._exit(0)
            break

        try:
            resposta = requests.post("http://127.0.0.1:8000/chat", json={"mensagem": msg}, stream=True)
            print("> IA: ", end="", flush=True)
            for linha in resposta.iter_lines():
                if linha:
                    print(linha.decode("utf-8"), end="", flush=True)
            print()
        except Exception as e:
            print(f"\n[ERRO] {e}\n")

if __name__ == "__main__":
    # Iniciar Ollama
    ollama_thread = threading.Thread(target=iniciar_ollama)
    ollama_thread.start()

    # Iniciar API
    api_thread = threading.Thread(target=iniciar_api)
    api_thread.start()

    # Aguardar a API
    if aguardar_api():
        chat_terminal()
    else:
        print("Erro: API não respondeu a tempo.")
        sys.exit(1)
