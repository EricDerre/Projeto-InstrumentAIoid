# Pesquisa — vocaloids e síntese de instrumentos (outubro de 2026)

Pesquisa feita em 6 a 9 de outubro de 2026 para orientar o InstrumentAIoid: a ideia de um "vocaloid" que canta e também faz o som de instrumentos.

## O que tem aqui

| Arquivo | O que é |
| --- | --- |
| `relatorio-vocaloids-e-instrumentos-2026-10.md` | Relatório principal, em português: apps de voz cantada, vozes famosas, o que dá para fazer de graça, integração com Cubase/FL Studio/REAPER e o caminho técnico do projeto. Comece por ele. |
| `notas-detalhadas-en/` | Notas de pesquisa completas, em inglês, com todas as fontes. Servem para aprofundar um assunto do relatório. |

### Notas detalhadas

| Arquivo | Assunto |
| --- | --- |
| `apps-comerciais-e-vozes-famosas.md` | VOCALOID6, Hatsune Miku (V6, NT2), Synthesizer V 2, Kasane Teto, CeVIO AI, VoiSona, ACE Studio e outros: versões, preços, vozes, idiomas. |
| `gratuitos-e-integracao-daw.md` | OpenUtau, UTAU, NEUTRINO, VOICEVOX, versões grátis dos comerciais, termos de uso das vozes, integração com DAWs e português. |
| `omnivocal-cubase15.md` | Omnivocal Beta (Yamaha) no Cubase 15: instalação, uso, limites e direitos. |
| `sintese-de-instrumentos.md` | Estado da arte em instrumentos "estilo vocaloid": Instrument X, ACE Studio, SWAM, DDSP, RAVE, datasets, o que roda numa GTX 1650. |
| `caminho-tecnico-do-projeto.md` | Arquitetura (OpenUtau + DiffSinger + DDSP), criação de vozes e bancos próprios, plug-ins para DAW, Python 3.14, LLM local e cuidados legais. |
| `pedal-miku-reaper.md` | Como imitar o pedal KORG Miku Stomp de graça no REAPER (ReaTune + Alter/Ego). |

## Resumo em 6 pontos

1. **Melhor app grátis:** OpenUtau com os bancos UTAU oficiais da Kasane Teto. Sem limite de trilhas, tem fonemizador de português (PT-BR CVC/BRAPA) e os termos da Teto deixam lançar e monetizar músicas como pessoa física.
2. **Melhor compra (se um dia quiser pagar):** Synthesizer V Studio 2 Pro (US$ 99 vitalício, roda na CPU, VST3 com ARA). A Hatsune Miku atual exige o VOCALOID6 (Miku V6, a partir de US$ 78 com o Editor Lite).
3. **Integração:** o REAPER é o único dos três hosts com ARA2, CLAP e VST3. Cubase LE/AI não tem ARA2 e o FL Studio 2024 não tem ARA. O caminho universal ainda é exportar WAV. O Omnivocal só funciona dentro do Cubase.
4. **A ideia do projeto já virou produto:** Dreamtonics Instrument X (agosto de 2026) e os instrumentos de IA do ACE Studio. O espaço livre é ser aberto, local, leve e em português.
5. **Caminho técnico sugerido:** OpenUtau + DiffSinger (ONNX) para a voz; MIDI → curvas de expressão → DDSP pequeno para instrumentos monofônicos; SFZ (sfizz) para polifônicos; treinar no Colab e renderizar no notebook; trocar o Mistral 7B por um modelo de 3–4B que caiba nos 4 GB de VRAM (ex.: ministral-3:3b), usando `/api/chat` com JSON Schema.
6. **Cuidado legal:** só usar vozes gravadas com consentimento por escrito; Crypton (Miku), Yamaha (Omnivocal) e a Teto proíbem ou restringem treinar IA com as vozes deles; atenção a pesos e datasets não comerciais (RAVE, MAESTRO, M4Singer, vocoder NSF-HiFiGAN comunitário).

## Próximos passos sugeridos para o InstrumentAIoid

- [ ] Definir o modelo de dados único: notas (com sílaba ou articulação) + curvas de afinação, dinâmica, ar e brilho.
- [ ] Instalar o OpenUtau e testar a Teto + um banco DiffSinger e o fonemizador PT-BR.
- [ ] Criar um ambiente Python 3.11 separado para as ferramentas de treino (DiffSinger, pc-ddsp).
- [ ] Trocar o modelo do Ollama por um de 3–4B e mudar `app/chat.py` para `/api/chat` com saída em JSON.
- [ ] Gravar a própria guitarra em várias notas e dinâmicas para um primeiro banco SFZ.

Fontes: todas as afirmações têm link no relatório e nas notas detalhadas.
