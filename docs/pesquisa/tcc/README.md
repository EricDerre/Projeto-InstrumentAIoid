<!-- ! Alteração de IA - Revisar: arquivo novo inteiro, índice das pesquisas copiadas do repositório do TCC (23/10/2026).
     ! Motivo: o Eric pediu para trazer do TCC o que serve ao InstrumentAIoid. Sem este índice, quem abrir a pasta não sabe o que cada arquivo responde, o que muda nesta máquina e que os links internos dos arquivos apontam para o TCC. -->

# Pesquisas trazidas do TCC

Cópia, sem alteração de texto, das pesquisas do repositório [EricDerre/TCC](https://github.com/EricDerre/TCC) (commit `362db9b`, 22/10/2026) que servem ao InstrumentAIoid. O original fica em `Documentacao/memorial/` do TCC; os links relativos dentro dos arquivos (para o Memorial, decisões e outros relatórios) apontam para lá e não funcionam aqui.

O TCC é um agente de QA que roda um LLM local só em CPU (Ollama). O assunto é outro, mas as perguntas de fundo são as mesmas deste projeto: que modelo cabe, como deixá-lo rápido em CPU, como fazer um modelo pequeno responder no formato certo e como dar memória a ele sem que ela vire erro.

## Antes de ler: o que muda nesta máquina

| No TCC | Aqui | Consequência |
|---|---|---|
| Fases 2-B em diante medidas num i5-1235U (2 núcleos P + 8 E), 16 GB, sem GPU | Acer Nitro 5: Ryzen 7 5800H (8 núcleos iguais, Zen 3), GTX 1650 4 GB, 16 GB | Os tempos do i5 valem como ordem de grandeza. A Fase 2-A do TCC rodou nesta máquina, e os números dela estão em [`../hardware-e-modelos-locais-2026-10.md`](../hardware-e-modelos-locais-2026-10.md) §3.1 |
| "Fixar threads nos núcleos P" | Ryzen não tem núcleos P/E | A lição vira: threads = núcleos físicos e reservar 2 núcleos para o jogo |
| Uma tarefa: escolher 1 de 23 causas | Conversa, escolha de módulo, decisão de jogo | O que vale para rótulo fechado vale para escolher módulo e ação; para a conversa livre, os ganhos de saída restrita não se aplicam |
| Um modelo por vez, nunca durante bateria | Jogo + IA ao mesmo tempo | A regra fica mais dura: um modelo pesado por vez e a GPU do jogo durante o jogo |
| Prompt pré-registrado, sem chamada de ferramentas | Orquestrador que chama módulos | Usar enum fechado de módulos no schema em vez de tool calling livre |

## O que tem aqui

| Arquivo | Responde | Uso no InstrumentAIoid |
|---|---|---|
| `literatura/modelos-locais-e-portugues.md` | Quais modelos livres rodam local e como vão em português | Escolha do LLM da persona: abaixo de 5B o português perde mais |
| `literatura/quantizacao.md` | Quanto se perde em 4 bits e no cache KV | Padrão Q4_K_M; não quantizar o cache KV |
| `literatura/medicao-em-cpu-e-estatistica.md` | Prefill contra geração, cache de prefixo, como comparar com poucos casos | Medir o orquestrador; persona fixa no começo do prompt |
| `literatura/tokenizacao-e-arquitetura.md` | Tokenização em português e inferência em CPU | Orçar contexto em caracteres por token |
| `literatura/raciocinio-em-estagios.md` | Se cadeia de pensamento ajuda modelos pequenos | Não ajuda: desligar *thinking*, saída curta |
| `literatura/documentacao-como-contexto-rag.md` | Como dar contexto a modelo pequeno sem confundi-lo | Memória e "lore" por recuperação top-3 |
| `literatura/memoria-gerida-pelo-modelo.md` | Memória que o próprio modelo escreve: ganhos e riscos | Memória de longo prazo da persona com portão em código |
| `literatura/levantamento-2026-09-22-llms-locais.md` | Levantamento completo de 22/09/2026: saída estruturada, CPU, RAG, cache, modelos 2025-2026 | Fonte das afirmações acima, com números e referências |
| `literatura/levantamento-2026-10-01-pre-fase-4.md` | Colibri, pesos lidos do disco, MoE em 16 GB, atlas de especialistas | Base da pesquisa de visualização em [`../brainiac-e-colibri-2026-10.md`](../brainiac-e-colibri-2026-10.md) |
| `literatura/referencias.md` | Lista ABNT de todas as fontes | Para achar o artigo citado por sobrenome e ano |
| `resultados/pre-fase-4-relatorio.md` | Vereditos sobre colibri, atlas e probabilidade do rótulo | Probabilidade do token como sinal de dúvida (AUROC 0,78) |
| `ferramental/ferramental-das-llms-locais.md` | Mapa adotado, adiado e descartado do ferramental do LLM local | Lista pronta do que configurar no Ollama |
| `ferramental/ferramental-do-claude-code.md` | Como o TCC usou o Claude Code (memória, hooks, skills, economia de tokens) | Complementa o CLAUDE.md deste repositório |

## O que ficou no TCC

Os relatórios de cada fase, as decisões numeradas e os dois levantamentos maiores (11/09/2026, 540 KB, e 29/09/2026, 228 KB, sobre documentação autogerida) são do problema do TCC e não foram copiados. Se a memória da persona crescer, o de 29/09 é o próximo a trazer.
