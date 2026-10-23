<!-- ! Alteração de IA - Revisar: arquivo novo inteiro, pesquisa sobre colibri e brainiac para visualizar a "rede neural" da IA (23/10/2026).
     ! Motivo: o Eric pediu para usar o colibri e pesquisar o brainiac à parte do TCC. O TCC já tinha lido o colibri por inteiro (levantamento de 01/10/2026, copiado em tcc/literatura/), então aqui fica o que muda para o InstrumentAIoid nesta máquina, sem repetir aquela leitura. -->

# Colibri e brainiac: como ver o "cérebro" da IA (outubro de 2026)

**Resposta curta:** o colibri é a única das fontes que mostra neurônios de verdade acendendo, mas só em modelos de mistura de especialistas (MoE), e nesta máquina só o OLMoE cabe. Nenhum dos projetos chamados "brainiac" que encontrei visualiza uma rede neural artificial. A proposta é um painel em três camadas, com o colibri como a camada "ao vivo" opcional.

## 1. Colibri

[JustVugg/colibri](https://github.com/JustVugg/colibri) é um motor de inferência em C para modelos MoE. Num MoE, cada camada tem muitos blocos de pesos (os especialistas) e um roteador escolhe poucos por token. O colibri deixa na RAM a parte que todo token usa e lê do disco os especialistas escolhidos. A leitura completa, com números, está em [`tcc/literatura/levantamento-2026-10-01-pre-fase-4.md`](tcc/literatura/levantamento-2026-10-01-pre-fase-4.md) §6.14.1 e o veredito em [`tcc/resultados/pre-fase-4-relatorio.md`](tcc/resultados/pre-fase-4-relatorio.md) §2 e §3.

### O que ele mostra (README lido em 23/10/2026)

- `coli web` sobe a API compatível com OpenAI e um painel no navegador.
- **Página Brain:** cada especialista roteado é uma célula; a cor diz onde o peso está (VRAM, RAM, disco), o brilho diz quanto é usado e os especialistas usados no turno piscam em branco. Passar o mouse mostra a afinidade de tópico medida.
- **Página Atlas:** vista 3D dos especialistas caracterizados, agrupados por tópico. A posição é afinidade de roteamento medida, não significado.
- **Telemetria:** o arquivo `.coli_usage` registra, a cada turno, quais especialistas foram usados. É o gancho para levar esses dados a um painel nosso.
- Roda no Windows (binários com `colibri.exe` e `coli.cmd`), com GPU opcional.

### O que cabe nesta máquina (Ryzen 7 5800H, 16 GB, GTX 1650 4 GB)

| Modelo do colibri | Disco | RAM pedida | Serve aqui? |
|---|---|---|---|
| OLMoE (7B no total, 1B ativo) | ~7 GB (int8) | 8 GB | Sim, fora do modo jogo. Num Apple M3 de 16 GB rodou a 3,69 a 4,18 tok/s; não há medida em Ryzen |
| DeepSeek V4 Flash, Qwen3.8-Flash-Next | ~167 e ~186 GB | 16 GB no mínimo | Não: sem folga de RAM, e nas máquinas de 24 a 32 GB medidas a resposta leva minutos |
| GLM-5.2 e maiores | 195 GB a 1,6 TB | 16 a 32 GB ou mais | Não |

### Veredito para o InstrumentAIoid

- **Não é o cérebro da persona.** O OLMoE fica abaixo do Qwen2.5-7B em qualidade (MMLU 54,1 contra 66,9 do Llama 3.1-8B na mesma avaliação, modelos base) e não foi avaliado em português; com 8 GB de RAM, não roda junto com um jogo.
- **Serve como "modo vitrine".** Fora do jogo, o orquestrador pode mandar uma pergunta ao OLMoE no colibri com o painel Brain aberto, e o Eric vê os especialistas acendendo enquanto a IA responde. É o mais perto de "ver a rede neural pensando" que roda nesta máquina.
- **O método do Atlas serve sem o colibri.** O TCC aplicou o método à própria busca (`gerar_atlas.py`): contar o que é acionado por tipo de pedido, corrigir pela taxa de base e exigir repetição. Aqui, o mesmo vale para o orquestrador: quais módulos e memórias são acionados por tipo de pedido.

## 2. Brainiac

"Brainiac" não aparece no TCC. Os projetos com esse nome que encontrei:

| Projeto | O que é | Serve para ver a rede neural? |
|---|---|---|
| [bornostojak/brainiac](https://github.com/bornostojak/brainiac) | Serviço em Go com SQLite, painel no navegador e MCP: agentes registram progresso, artigos de conhecimento e lições aprendidas. Instala skills no Claude Code | Não. Mostra o trabalho dos agentes, não a rede. Projeto novo (0 estrelas, 28 commits), sem autenticação |
| [imMohammedSahil/Brainiac](https://github.com/imMohammedSahil/Brainiac) | Plataforma com cérebro humano 3D (React Three Fiber) colorido por questionário | Não mostra ativações artificiais, mas o código de cena 3D (carregar GLB, destacar regiões, cores por valor) serve de base para um "cérebro" visual alimentado por dados ao vivo |
| [AIM-KannLab/BrainIAC](https://github.com/AIM-KannLab/BrainIAC) | Modelo de fundação para ressonância magnética do cérebro | Não, é de medicina |

**Pergunta em aberto para o Eric:** se o brainiac da sua pesquisa for outro, me manda o link.

## 3. Proposta: o painel do "cérebro" em três camadas

| Camada | Mostra | Ferramenta | Quando roda |
|---|---|---|---|
| Estrutura | As camadas de cada modelo (RVC, YOLO, DiffSinger) | Netron, já configurado em `tools/ver_rede.py` | Sob demanda |
| Orquestrador ao vivo | Qual módulo foi chamado, quais memórias entraram, a probabilidade da escolha, o modo atual | Painel próprio lendo os eventos do orquestrador; cena 3D no estilo do Brainiac de cérebro humano, com uma região por módulo | Sempre, inclusive no jogo (é leve) |
| Neurônios ao vivo | Especialistas de um MoE acendendo por token | Colibri com OLMoE e a página Brain | Só no modo conversa ou estúdio |

A segunda camada é a que mostra o comportamento da IA do projeto. A terceira mostra uma rede de verdade, mas a de um modelo auxiliar.

## Fontes

- [JustVugg/colibri, README](https://raw.githubusercontent.com/JustVugg/colibri/main/README.md) (lido em 23/10/2026)
- Levantamento e relatório da Pré-Fase 4 do TCC, em `tcc/`
- [bornostojak/brainiac](https://github.com/bornostojak/brainiac)
- [imMohammedSahil/Brainiac](https://github.com/imMohammedSahil/Brainiac)
- [AIM-KannLab/BrainIAC](https://github.com/AIM-KannLab/BrainIAC)
