from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from app.chat import stream_resposta_do_ollama

app = FastAPI()

class Mensagem(BaseModel):
    mensagem: str

@app.post("/chat")
def chat(mensagem: Mensagem):
    stream = stream_resposta_do_ollama(mensagem.mensagem)
    return StreamingResponse(stream, media_type="text/plain")