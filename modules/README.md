<!-- ! Alteração de IA - Revisar: arquivo novo inteiro, contrato que todo módulo do InstrumentAIoid segue (23/10/2026).
     ! Motivo: a regra do CLAUDE.md diz que cada skill é um módulo isolado em modules/<nome>/, mas não dizia como um módulo se apresenta para a IA central. Com o contrato escrito antes do primeiro módulo, voz, jogo e avatar nascem com a mesma forma e a IA central não precisa de código especial para cada um. -->

# Módulos

Cada habilidade da IA é um módulo em `modules/<nome>/`. Um módulo funciona sozinho (pela linha de comando) e também pode ser chamado pela IA central (pela API local). A arquitetura completa está em [`docs/arquitetura.md`](../docs/arquitetura.md).

## Módulos planejados

| Pasta | Faz | Etapa do plano |
|---|---|---|
| `voz/` | STT, TTS na CPU e conversão RVC com o modelo do Eric | 3 |
| `avatar/` | Ponte com o modelo VRM: lip sync, gestos, reação a cliques | 5 |
| `instrumental/` | MIDI e curvas de expressão para áudio (DDSP, SFZ), canto via OpenUtau, separação de faixas com UVR5 | 6 |
| `visao/` | Captura de tela, detecção e OCR, estado do jogo | 7 |
| `jogo/` | Reflexo rápido (política treinada) e envio de teclas | 7 |

A conversa com a persona não é um módulo: é a própria IA central (hoje em `app/`).

## O contrato

Todo módulo tem as quatro peças abaixo.

**1. `manifesto.json`**, lido pela IA central para saber que o módulo existe:

```json
{
  "nome": "voz",
  "descricao": "Fala um texto com a voz da persona. Use para toda resposta falada.",
  "entrada": {"type": "object", "properties": {"texto": {"type": "string"}, "emocao": {"enum": ["neutra", "alegre", "triste"]}}, "required": ["texto"]},
  "saida": {"type": "object", "properties": {"arquivo_wav": {"type": "string"}, "duracao_s": {"type": "number"}}},
  "recursos": {"ram_mb": 1500, "vram_mb": 0, "nucleos": 2},
  "modos": ["conversa", "jogo", "estudio"]
}
```

- `descricao` é o texto que o LLM lê para decidir; uma frase, dizendo quando usar.
- `recursos` é o orçamento declarado, medido na máquina do Eric. A IA central usa isso para decidir o que carregar em cada modo.
- `modos` diz em quais modos o módulo pode ficar carregado.

**2. Interface em Python** (`__init__.py`):

```python
def iniciar() -> None: ...                 # carrega modelos; chamado ao entrar num modo que usa o módulo
def executar(pedido: dict) -> dict: ...    # pedido segue "entrada", resposta segue "saida"
def estado() -> dict: ...                  # pronto, ocupado ou erro, e o que está carregado
def parar() -> None: ...                   # descarrega tudo e libera RAM e VRAM
```

Sem estado global compartilhado com outros módulos: o que o módulo precisa vem no pedido.

**3. Duas portas:**

- Linha de comando, para usar sozinho: `python -m modules.voz "olá"`.
- API local, para a IA central: as mesmas quatro funções expostas por HTTP ou WebSocket em `127.0.0.1`.

**4. Teste de fumaça** em `tests/`, que roda sem LLM e sem GPU, para conferir o módulo antes de ligá-lo ao resto.

## Como a IA central escolhe o módulo

Os manifestos viram um enum fechado no JSON Schema da resposta do LLM (`"modulo": {"enum": ["voz", "avatar", ...]}`), e o pedido é validado contra `entrada` em código antes de ser executado. Não se usa chamada de ferramentas livre: com modelo pequeno, o TCC mediu que o formato imposto pelo motor e um conjunto fechado de opções funcionam melhor (ver `docs/pesquisa/tcc/`).
