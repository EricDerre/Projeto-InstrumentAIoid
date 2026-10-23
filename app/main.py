from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from app.chat import stream_resposta_do_ollama

# ! Alteração de IA - Revisar: imports do painel do cérebro.
# ! Motivo: servir a página /cerebro e o fluxo de eventos dela.
from pathlib import Path
from fastapi.responses import FileResponse
from app.cerebro import emitir, fluxo_sse

app = FastAPI()

class Mensagem(BaseModel):
    mensagem: str

@app.post("/chat")
def chat(mensagem: Mensagem):
    # ! Alteração de IA - Revisar: evento de entrada da mensagem.
    # ! Motivo: o painel mostra a seta usuário -> central quando chega uma mensagem.
    emitir("usuario", "central", "pedido", mensagem.mensagem[:80])
    stream = stream_resposta_do_ollama(mensagem.mensagem)
    return StreamingResponse(stream, media_type="text/plain")


# ! Alteração de IA - Revisar: três rotas novas do painel do cérebro.
# ! Motivo: /cerebro abre o painel no navegador, /cerebro/eventos manda os eventos ao vivo,
# e /cerebro/evento deixa módulos em outro processo (visão, voz) registrarem eventos.
class Evento(BaseModel):
    origem: str
    destino: str
    tipo: str = "estado"
    resumo: str = ""
    dados: dict = {}

@app.get("/cerebro")
def painel_cerebro():
    return FileResponse(Path(__file__).parent / "static" / "cerebro.html")

@app.get("/cerebro/eventos")
def eventos_cerebro():
    return StreamingResponse(fluxo_sse(), media_type="text/event-stream")

@app.post("/cerebro/evento")
def registrar_evento(evento: Evento):
    return emitir(evento.origem, evento.destino, evento.tipo, evento.resumo, **evento.dados)
