<!-- ! Alteração de IA - Revisar: arquivo novo inteiro. -->
<!-- ! Motivo: dar ao Claude Code, em toda sessão, o objetivo, as regras e os comandos do projeto sem ele ter que descobrir sozinho. Manter curto: cada linha aqui custa contexto em toda sessão. -->

# InstrumentAIoid

IA estilo vocaloid que canta, faz som de instrumentos (guitarra, piano, synth), conversa com persona própria, tem avatar animado e joga jogos só vendo a tela.

## Regras do projeto

- Cada skill é um módulo isolado em `modules/<nome>/`, usável sozinho e com interface pequena. A IA central só chama essas interfaces, nunca o interior de um módulo.
- Tudo roda na máquina do Eric (hardware modesto, jogo + IA ao mesmo tempo). Todo modelo novo precisa de um orçamento de VRAM/RAM declarado no CLAUDE.md do módulo.
- Ferramentas externas locais (Ultimate Vocal Remover v5, Applio/RVC, Ollama) são chamadas por scripts Python com linha de comando.
- Nunca fazer commit, `git add`, push ou PR: o Eric faz. Nada destrutivo sem confirmação.
- Todo trecho alterado por IA leva `! Alteração de IA - Revisar: <o quê>` e, na linha seguinte, `! Motivo: <por quê>`, em português simples.
- Escrever em português.

## Comandos

- Rodar o chat: `python instrumentaloid.py` (sobe Ollama + API FastAPI em 127.0.0.1:8000).
- Ver a estrutura de um modelo: `python tools/ver_rede.py <arquivo do modelo>` (abre o Netron no navegador).
- Painel do cérebro: com a API rodando, abrir http://127.0.0.1:8000/cerebro. Módulos registram eventos com `app.cerebro.emitir(...)` ou POST em `/cerebro/evento`.
- Testes: `pytest` (ainda não há testes; todo módulo novo deve vir com eles).

## Onde está o quê

- `app/`: API FastAPI, cliente do Ollama e painel do cérebro (`cerebro.py`, `static/cerebro.html`).
- `tools/`: scripts de apoio que rodam na máquina local.
- `docs/pesquisa/`: pesquisas grandes (25 a 68 KB cada). Ler `docs/pesquisa/README.md` primeiro e abrir só a nota necessária.
- `build/` e `instrumentaloid.exe`: gerados pelo PyInstaller. Não ler.
