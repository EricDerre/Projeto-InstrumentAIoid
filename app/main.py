from fastapi import FastAPI
from chat import gerar_resposta

app = FastAPI()

@app.post("/chat")
async def chat_endpoint(prompt: str):
    resposta = gerar_resposta(prompt)
    return {"resposta": resposta}