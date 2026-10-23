<!-- ! Alteração de IA - Revisar: arquivo novo inteiro, resumo da arquitetura modular e do plano em etapas (23/10/2026).
     ! Motivo: a arquitetura foi escrita num documento do claude.ai; sem uma cópia curta no repositório, quem trabalha no código (inclusive o Claude Code) não a encontra. -->

# Arquitetura do InstrumentAIoid

Documento completo, com diagrama, fontes e o que veio do TCC: [InstrumentAIoid: arquitetura modular e o que vem do TCC](https://claude.ai/artifact/6x1uGWK1pyWZx4XdQSfmq5).

## Em uma frase

Uma IA central (orquestrador em Python com LLM local) recebe eventos, escolhe qual módulo chamar com uma resposta em JSON presa por schema, valida em código e executa; cada módulo também roda sozinho.

```
 Microfone (STT)   Tela do jogo   Chat e texto   Cliques no avatar
        \               |              |               /
         +-------- Orquestrador central (LLM local) --------+
         |  persona + memória (BM25, top-3) em ordem fixa   |
         |  gerente de recursos: modo conversa/jogo/estúdio |
         +----+---------+----------+---------+---------+----+
              |         |          |         |         |
             voz   instrumental  visao     jogo     avatar
```

## Regras que sustentam a arquitetura

1. **Um modelo pesado carregado por vez.** O gerente de recursos troca de modo e chama `iniciar()`/`parar()` dos módulos. Orçamento por modo em [`pesquisa/hardware-e-modelos-locais-2026-10.md`](pesquisa/hardware-e-modelos-locais-2026-10.md) §2.
2. **Durante o jogo, a GPU é do jogo.** A IA roda na CPU, com 2 núcleos reservados para o jogo.
3. **Jogo em duas camadas.** Um reflexo rápido (10 a 30 decisões por segundo, modelos pequenos e código) e o LLM só como estrategista, a cada poucos segundos. Jogar só pelo modelo de visão e linguagem falha até em modelos grandes.
4. **Toda saída do LLM é validada em código** antes de virar ação: o formato pode estar certo com o conteúdo errado.
5. **Contrato único de módulo**, em [`../modules/README.md`](../modules/README.md).

## Plano em etapas

| Etapa | Entrega | Pronto quando |
|---|---|---|
| 1. Base e medição | Pastas, pesquisas do TCC em `docs/pesquisa/tcc/`, script que mede RAM, VRAM e CPU livres com e sem jogo | O orçamento por modo tem números medidos |
| 2. Persona em texto | Qwen2.5 7B ou 3-4B, `/api/chat` com schema, cartão de personagem, memória com BM25 e validador | 30 minutos de conversa sem perder a persona, com memória entre sessões |
| 3. Voz própria | `modules/voz/`: STT, TTS na CPU, RVC frase a frase | Resposta falada com a voz do Eric, primeira palavra em até ~2 s |
| 4. Orquestrador | Manifestos, enum de módulos, gerente de recursos | "Fala isso cantando" escolhe o módulo certo; módulos seguem rodando sozinhos |
| 5. Avatar | `modules/avatar/`: ponte VRM, lip sync, gestos | Clique no avatar gera reação; boca acompanha a fala |
| 6. Instrumental e canto | `modules/instrumental/`: OpenUtau + DiffSinger, DDSP, SFZ, UVR5 por script | Melodia MIDI vira guitarra ou piano e canto com a voz RVC |
| 7. Jogo por visão | `modules/visao/` e `modules/jogo/` num jogo lento primeiro | A IA passa uma fase rodando junto com o jogo, sem ler dados internos dele |

A etapa 6 não depende da 5 e pode andar em paralelo.

## O que ainda não mudou no código

`app/` continua sendo a semente do orquestrador e não foi movido, porque `instrumentaloid.py` e `instrumentaloid.spec` dependem desse caminho. A mudança de `app/` para o orquestrador entra na etapa 4.
