# ! Alteração de IA - Revisar: arquivo novo inteiro.
# ! Motivo: registrar o que a IA central faz (qual módulo chamou, o que recebeu, quanto
# demorou) para o painel /cerebro mostrar ao vivo. Não usa GPU: só guarda pequenos eventos.
"""Barramento de eventos do "cérebro" da IA central.

Qualquer parte do código chama `emitir(...)`. O painel em /cerebro recebe os eventos
ao vivo por SSE. Módulos que rodam em outro processo (visão do jogo, voz) mandam
eventos por POST em /cerebro/evento, com o mesmo formato.
"""

import asyncio
import json
import threading
import time
from collections import deque

_HISTORICO_MAX = 200

_historico = deque(maxlen=_HISTORICO_MAX)
_assinantes = []  # pares (loop, fila) de cada navegador conectado
_trava = threading.Lock()


def emitir(origem: str, destino: str, tipo: str, resumo: str = "", **dados):
    """Registra um evento: `origem` mandou algo para `destino`.

    tipo: "pedido", "resposta", "erro" ou "estado" (o painel colore por tipo).
    resumo: texto curto para o log do painel.
    """
    evento = {
        "t": time.time(),
        "origem": origem,
        "destino": destino,
        "tipo": tipo,
        "resumo": resumo[:200],
        "dados": dados,
    }
    with _trava:
        _historico.append(evento)
        assinantes = list(_assinantes)
    # O endpoint /chat roda numa thread separada, então a fila é alimentada
    # pelo loop de cada conexão, do jeito seguro entre threads.
    for loop, fila in assinantes:
        loop.call_soon_threadsafe(fila.put_nowait, evento)
    return evento


async def fluxo_sse():
    """Gera o fluxo SSE: primeiro o histórico recente, depois os eventos novos."""
    loop = asyncio.get_running_loop()
    fila = asyncio.Queue()
    with _trava:
        recentes = list(_historico)
        _assinantes.append((loop, fila))
    try:
        for evento in recentes:
            yield _formatar(evento)
        while True:
            try:
                evento = await asyncio.wait_for(fila.get(), timeout=15)
                yield _formatar(evento)
            except asyncio.TimeoutError:
                yield ": ping\n\n"  # mantém a conexão aberta
    finally:
        with _trava:
            _assinantes.remove((loop, fila))


def _formatar(evento):
    return f"data: {json.dumps(evento, ensure_ascii=False)}\n\n"
