<!-- ! Alteração de IA - Revisar: arquivo criado em 23/10/2026 (pesquisa e medição de RAM, quantização e RAG/memória da persona).
     ! Também (23/10, tarde): a persona se chama SennAI; "Astolfo" é só o modelo de voz RVC. Trocado o nome nas seções 4 e 5 e apontado o script comparar_persona.py.
     ! Motivo: o Eric não pode aumentar a RAM agora e pediu para continuar as pesquisas de otimização, quantização e RAG; os números saem de bench/bench_ram*.py e bench/bench_embed.py. -->
# Caber nos 16 GB: RAM, quantização e memória da persona (outubro de 2026)

Continuação de [hardware-e-modelos-locais-2026-10.md](hardware-e-modelos-locais-2026-10.md). Lá apareceu que, com o Warcraft III aberto, sobrava só ~1 GB de RAM livre. Como trocar a RAM não é possível agora, aqui está **quanto cada peça gasta de verdade** e **o que fazer para tudo caber**.

Todos os números marcados **[medido]** foram tirados nesta máquina em 23/10/2026, com os scripts `bench/bench_ram.py`, `bench/bench_ram_llm.py`, `bench/bench_ram_rvc.py` e `bench/bench_embed.py`. "RAM residente" é o *working set*: o que o processo ocupa na RAM física naquele momento.

---

## 1. Resumo

1. **O maior ladrão de RAM não é a IA: são os programas abertos.** Firefox, o app do Claude, WebView2, Steam, Discord, Wallpaper Engine, Voicemod, Parsec e Teams somam **~6 GB residentes e ~9 GB de memória privada**. Com eles abertos, mesmo sem jogo, só havia 4,7–6,4 GB livres e o Windows já usava 4,8 GB do arquivo de paginação **[medido]**. Fechar esses programas no modo Jogando vale mais que qualquer quantização.
2. **O pacote completo da IA no modo Jogando cabe em ~5,5 GB residentes**: LLM 3B (2,1–2,5 GB), RVC (1,9 GB), Whisper + Piper + YOLO (~0,5 GB) e embeddings (0,3–0,65 GB) **[medido]**. Com o jogo (~3 GB no Warcraft III) e o Windows (~3 GB), dá ~11,5 GB dos 15,4 GB. **Cabe**, desde que o resto esteja fechado.
3. **O `llama3.2:3b` em Q3_K_M economizou 310 MB e ficou mais rápido** (17,3 contra 14,9 tok/s), e a resposta continuou boa **[medido]**. Abaixo de Q3_K_M a perda de qualidade fica clara **[fonte]**.
4. **Não ligar o mmap no Windows:** o Ollama já carrega sem mmap (`--load-mode none`), e ligar `use_mmap` **aumentou** a RAM residente em 1,3–1,7 GB **[medido]**.
5. **Cache KV em q8_0 economiza pouco (200–280 MB) e deixou a geração 20–25% mais lenta** na CPU **[medido]**. Só vale se faltar memória por pouco.
6. **O RVC é a peça mais cara por função:** o processo do Applio com PyTorch e CUDA ocupa ~1,9 GB residentes e reserva ~6 GB de memória virtual **[medido]**. O modo ONNX do Applio não ajudou (2,2 GB).
7. **Para a memória da persona, embeddings ganham do BM25 em conversa:** o `embeddinggemma` acertou 5 de 6 perguntas usando 0,65 GB, contra 2 de 6 do BM25 **[medido]**. É o contrário do que o TCC achou para vocabulário técnico, então o certo é usar os dois juntos.

---

## 2. Para onde vai a RAM hoje

Sem jogo aberto, às 13:30 de 23/10/2026 **[medido]**:

| Programa | Processos | RAM residente | Memória privada |
|---|---|---|---|
| Firefox | 16 | 2,0 GB | 2,5 GB |
| Claude (app) | 9 | 1,0 GB | 1,3 GB |
| WebView2 (usado por vários apps) | 13 | 0,4 GB | 1,2 GB |
| Steam (webhelper + cliente) | 9 | 0,3 GB | 1,2 GB |
| Discord | 6 | 0,6 GB | 0,7 GB |
| Gerenciador de janelas (dwm) | 1 | 0,2 GB | 0,6 GB |
| Antivírus (MsMpEng) | 1 | 0,35 GB | 0,56 GB |
| Wallpaper Engine | 1 | 0,2 GB | 0,5 GB |
| Voicemod, Parsec, SourceTree, Teams, Área de Trabalho Remota | — | ~0,5 GB | ~1,3 GB |

Total da máquina: 15,4 GB, **6,4 GB livres**, 19,1 GB de memória comprometida (RAM + paginação) e **4,8 GB já no arquivo de paginação** (pico de 8,2 GB).

O que dá para fazer, do mais forte para o mais fraco:

- **Fechar** Firefox (ou deixar uma aba só), Discord, Teams, Voicemod, Parsec, SourceTree e a Área de Trabalho Remota no modo Jogando: ~3,5–4 GB.
- **Pausar o Wallpaper Engine** (ele tem opção de pausar quando outro app está em tela cheia): ~0,2–0,5 GB, mais uns 100–200 MB de VRAM.
- **Steam:** em jogos da Steam o cliente precisa ficar aberto, mas dá para desligar o navegador interno nas configurações. No Warcraft III ele nem é necessário.
- O orquestrador da IA pode ter um "modo Jogando" que **lista** o que está aberto e gastando RAM e **pergunta** antes de fechar. Fechar programas do usuário sem perguntar não é uma boa ideia.

---

## 3. Quanto cada módulo da IA gasta

### 3.1 LLM (Ollama 0.40.8, só CPU, processo `llama-server.exe`) **[medido]**

| Modelo e configuração | RAM residente | Geração |
|---|---|---|
| `qwen3:1.7b`, contexto 4096 | ~1,5 GB | 19 tok/s |
| `llama3.2:3b` (Q4_K_M), contexto 4096 | 2,45 GB | 14,9 tok/s |
| **`llama3.2:3b-instruct-q3_K_M`**, contexto 4096 | **2,14 GB** | **17,3 tok/s** |
| `llama3.2:3b`, cache KV q8_0 | 2,24 GB | 11,1 tok/s |
| `llama3.2:3b` com `use_mmap: true` | 3,75 GB | 12,0 tok/s |
| `qwen3:4b-instruct` (Q4_K_M), contexto 4096 | 3,05 GB | 11,0 tok/s |
| `qwen3:4b-instruct`, contexto 2048 | 2,76 GB | 9,8 tok/s |
| `qwen3:4b-instruct`, cache KV q8_0 | 2,77 GB | 8,8 tok/s |
| `qwen3:4b-instruct`, cache KV q8_0, contexto 8192 | 3,08 GB | 8,7 tok/s |

A velocidade varia ±15% entre rodadas, porque os outros programas abertos disputavam a CPU. As diferenças de RAM são estáveis.

O que isso diz:

- **Q3_K_M no 3B é o melhor ganho:** menos RAM e mais velocidade, porque em CPU cada token custa ler os pesos inteiros da RAM. A resposta de teste continuou natural ("Estou aqui para tudo! Gosto de tocar instrumentos, cantar…"). Precisa de um teste de qualidade maior antes de virar padrão (seção 4).
- **Contexto de 2048 economiza ~290 MB no 4B.** Para conversa durante o jogo, 2048 tokens bastam se o orquestrador resumir o histórico antigo. O TCC mostrou que o Ollama **corta o começo do prompt em silêncio** quando o contexto estoura, e o começo é a persona. Então o orquestrador precisa contar tokens antes de mandar.
- **Cache KV q8_0:** liga com as variáveis `OLLAMA_KV_CACHE_TYPE=q8_0` e `OLLAMA_FLASH_ATTENTION=1`, que valem para o servidor inteiro. Para testar, subi um Ollama separado na porta 11435 e não mudei o seu. Economiza pouco com contexto curto, porque o cache é pequeno nesses modelos, e a flash attention na CPU deixou a geração mais lenta. O TCC já tinha encontrado essa lentidão na literatura (até 26% mais lenta na CPU). Vale para contextos longos (8192+), não para o modo Jogando.
- **mmap:** no Windows, ligar o mmap faz os pesos serem contados duas vezes (cópia mapeada + buffers). O padrão do Ollama (`--load-mode none`) é o certo aqui. A documentação do llama.cpp diz que desligar o mmap "pode reduzir *pageouts*" quando não se usa `mlock` **[fonte]**.

### 3.2 Voz, escuta e visão (incremento ao carregar no mesmo processo Python) **[medido]**

| Peça | RAM residente a mais |
|---|---|
| Piper `pt_BR-faber-medium` | ~0,1 GB (+0,5 GB de memória privada do ONNX Runtime na primeira importação) |
| Kokoro (`pf_dora`) | ~0,37 GB |
| faster-whisper `base` int8 | ~0,15 GB |
| faster-whisper `small` int8 | ~0,17 GB |
| YOLO26n 320 px na Radeon (DirectML) | ~0,07 GB |

Tudo isso é barato. **Colocar Piper, Whisper e YOLO num mesmo processo** evita carregar o ONNX Runtime três vezes.

### 3.3 RVC (Applio com o astolfoV3 na GPU) **[medido]**

| Momento | RAM residente | Memória privada (reservada) |
|---|---|---|
| Python vazio | 18 MB | 10 MB |
| Depois de importar PyTorch + CUDA | 0,65 GB | 3,8 GB |
| Modelo carregado e uma conversão feita (motor torch) | **1,9 GB** | 6,1 GB |
| O mesmo com o decodificador ONNX do Applio (FP32) | 2,2 GB | 7,5 GB |

- A memória privada alta é quase toda reserva das bibliotecas CUDA. Ela não ocupa RAM física, mas **conta para o limite de memória comprometida**. Por isso o arquivo de paginação precisa continuar "gerenciado pelo sistema" (hoje tem 17 GB, o que basta).
- O ONNX do Applio com FP16 **falhou** ("ONNX decoder produced non-finite audio"), mesmo problema de FP16 da série GTX 16. Com FP32 funcionou, mas gastou mais RAM. **Ficar com o motor torch.**
- O RVC precisa ficar carregado o jogo inteiro (a primeira conversão leva ~45 s). Ele é o candidato natural a dividir processo com o TTS: um "servidor de voz" que recebe texto e devolve áudio já convertido.

### 3.4 Embeddings para a memória (Ollama, só CPU) **[medido]**

10 memórias curtas sobre o Eric e 6 perguntas parafraseadas ("qual o nome do meu bichinho?" → "O gato do Eric se chama Pixel."):

| Modelo | RAM residente | ms por memória | ms por consulta | Acertos (top-1) |
|---|---|---|---|---|
| BM25 (SQLite FTS5) | ~0 | — | <1 | 2/6 |
| `nomic-embed-text` | 0,29 GB | 31 | 44 | 2/6 |
| **`embeddinggemma`** (300M) | 0,65 GB | 22 | 42 | **5/6** |
| `qwen3-embedding:0.6b` | 1,1 GB | 83 | 82 | 5/6 |

O `embeddinggemma` empata com o `qwen3-embedding` no acerto, usa metade da RAM e é 2× mais rápido. O `nomic-embed-text` (que já estava instalado) é fraco em português. Seis perguntas é pouco para uma conclusão firme, mas a diferença foi grande.

---

## 4. Quantização: até onde dá para descer

O que a pesquisa diz, somando o TCC e fontes de 2026:

- **4 bits (Q4_K_M) é praticamente sem perda** em modelos grandes. Em 55 quantizações do Qwen3.6 27B, Q4_K_M ficou indistinguível do original; Q8_0 bateu o token mais provável do BF16 em 99,3% das vezes **[fonte: Quesma, jul/2026]**.
- **3 bits é instável e depende da receita:** no mesmo estudo, Q3_K_M marcou 73,3% no AIME-120 (o original marcou 70,8%), mas Q3_K_S caiu para 54,2%. A queda acompanha a divergência KL em relação ao original: abaixo de 0,05 ficou perto do original, acima de 0,08 caiu sempre **[fonte: Quesma]**.
- **O que se perde primeiro é conhecimento factual** (trivia), não código nem forma **[fonte: Quesma, ago/2026]**. Para a SennAI isso pesa pouco, porque o que ela precisa saber vem da memória recuperada (RAG), não dos pesos.
- **Modelos pequenos sofrem mais:** a 4 bits, o Llama-3.2-1B perde 10,1 pontos (GPTQ) e 16 pontos em seguir instruções, enquanto o 3B perde só 1,8 **[fonte: Lee et al., IJCAI 2025, via TCC]**. Modelos pequenos treinados com muitos dados (Qwen) são os mais expostos **[fonte: Ouyang et al., ACL 2025, via TCC]**.
- **2 bits: perda clara** em todos os testes **[fonte: Quesma]**.
- **Na CPU, evitar os quants "I" (IQ3, IQ4_XS):** o prefill cai pela metade **[fonte: Kawrakow 2024, via TCC]**.

Na prática:

| Modelo | Quantização sugerida | Por quê |
|---|---|---|
| 3B (llama3.2) | **Q3_K_M** no modo Jogando, Q4_K_M fora dele | medido: −310 MB e mais rápido; 3B aguenta 3 bits melhor que 1B |
| 4B (qwen3-instruct) | Q4_K_M | não achei tag Q3 oficial no Ollama; Q3 de terceiros precisa de teste |
| 1–2B | Q4_K_M ou Q8_0, nunca Q3 | os pequenos degradam mais |

**Teste de qualidade:** 25 falas da SennAI comparando Q4_K_M e Q3_K_M às cegas, julgadas pelo Eric (o que importa é a persona, não um benchmark). Script `bench/comparar_persona.py`; respostas em `bench/resultados/persona_avaliacao.md` e chave em `persona_chave.json`.

---

## 5. Memória da persona (RAG)

### 5.1 O que o TCC já ensinou e vale aqui

- **Recuperar os 3 mais relevantes ganha de "tudo no prompt"** em modelos pequenos, e o meio de um contexto longo é onde o modelo mais erra (*lost in the middle*) **[fonte: TCC, §6.3]**.
- **O modelo segue memória errada:** no TCC, documentação errada foi seguida em 93–96% dos casos **[medido no TCC]**, e em modelos grandes passa de 60% **[fonte: ClashEval, via TCC]**. Toda memória que a SennAI escrever sobre o Eric precisa passar por **validação em código** antes de entrar (formato, tamanho, não contradizer o que já existe, nunca apagar sozinha).
- **Cache de prefixo:** o Ollama reaproveita o começo igual do prompt **[medido no TCC]**. A ordem precisa ser: **persona fixa → memórias recuperadas → histórico recente → fala nova**. Se a memória vier antes da persona, o cache da persona se perde a cada fala.
- **Pedaços inteiros, sem fatiar:** cada memória é uma frase ou um parágrafo curto, indexado inteiro **[fonte: TCC, §6.12.3]**.

### 5.2 O que muda em relação ao TCC

No TCC, o BM25 ganhava porque a busca era por vocabulário técnico (nomes de campo, códigos HTTP). Numa conversa as pessoas parafraseiam ("bichinho" para gato, "instrumento" para guitarra), e aí o BM25 acertou só 2 de 6 **[medido]**. Então:

- **Busca híbrida:** `embeddinggemma` (sentido) + BM25 do SQLite (nomes próprios, títulos de música, nomes de jogo), juntados por **RRF** (fusão por posição), que no TCC foi o ganho mais barato **[fonte: Akarsu et al., 2026, via TCC]**.
- **Armazenamento simples:** um arquivo SQLite com uma tabela FTS5 (BM25 já vem no SQLite) e os vetores como coluna binária. Para alguns milhares de memórias, comparar vetores com NumPy leva milissegundos. **Não precisa de banco vetorial.**
- **Prefixos do embeddinggemma:** consultas com `task: search result | query: ` e memórias com `title: none | text: ` **[fonte: Hugging Face]**.
- **Dá para encolher o vetor** de 768 para 256 dimensões (Matryoshka) sem trocar de modelo **[fonte: Hugging Face]**.

### 5.3 Tipos de memória sugeridos

| Tipo | Exemplo | Quando entra no prompt |
|---|---|---|
| Persona (fixa) | quem a SennAI é, jeito de falar | sempre, no começo (fica no cache) |
| Fatos do usuário | "o Eric toca guitarra" | top-3 por busca híbrida |
| Episódios | "ontem perdemos 3 partidas seguidas no Warcraft" | top-2, com data |
| Estado do jogo | "vida 40%, 3 inimigos à direita" (vem do YOLO) | só no modo Jogando, no fim do prompt |
| Resumo da conversa | resumo do que passou do contexto | quando o histórico passa de ~1.500 tokens |

### 5.4 Ferramentas prontas (para comparar, não necessariamente usar)

Mem0, Letta (ex-MemGPT) e similares fazem isso de forma genérica, mas costumam chamar o LLM para decidir o que guardar, o que custa segundos de CPU a cada fala. Aqui é melhor **escrever memórias fora do caminho crítico** (depois que a fala terminou, ou quando o jogo pausa) e com regras em código.

---

## 6. Plano de memória do modo Jogando

| Peça | Escolha | RAM residente |
|---|---|---|
| Windows + essenciais (antivírus, dwm, drivers) | — | ~3 GB |
| Jogo (Warcraft III medido) | — | ~3 GB |
| LLM | `llama3.2:3b-instruct-q3_K_M`, contexto 2048, só CPU | ~2,0 GB |
| Servidor de voz (RVC na GPU + Piper) | um processo | ~2,0 GB |
| Escuta + visão (Whisper `small` int8 + YOLO26n na Radeon) | um processo | ~0,4 GB |
| Memória (embeddinggemma no Ollama + SQLite) | carregar sob demanda | ~0,65 GB |
| Orquestrador | Python | ~0,1 GB |
| **Total** | | **~11,2 GB de 15,4 GB** |

Para isso funcionar:

1. **Fechar os programas da seção 2** antes de jogar. O orquestrador pode listar o que está aberto e pedir confirmação.
2. **`OLLAMA_MAX_LOADED_MODELS=2`**, para o LLM e o embedding ficarem juntos sem um expulsar o outro. É uma variável global do Ollama, então só vale mudar quando o orquestrador existir.
3. **Embeddings das memórias já calculados e salvos.** Durante o jogo só se calcula o vetor da pergunta (~40 ms).
4. **Arquivo de paginação "gerenciado pelo sistema" e no NVMe** (já está assim). O RAM-compression do Windows ajuda, mas não deu para ver o estado sem permissão de administrador.
5. **Fora do jogo** dá para voltar ao `qwen3:4b-instruct` em Q4_K_M com contexto 4096, mais o Kokoro se a voz dele for melhor.

---

## 7. O que ainda falta medir

- qualidade da persona em Q3_K_M × Q4_K_M (teste com o Eric julgando);
- o pacote inteiro carregado ao mesmo tempo com o jogo, para conferir a soma da seção 6 e ver se o FPS do jogo cai;
- busca híbrida (RRF) num conjunto maior de memórias, com 30–50 perguntas;
- Kokoro e RVC dividindo o mesmo processo PyTorch (versão torch do Kokoro), para ver se economiza RAM.

---

## Fontes

Medições desta máquina (23/10/2026): `bench/resultados/ram.jsonl` e `bench/resultados/ram_llm.jsonl`, gerados pelos scripts citados no topo.

TCC ([github.com/EricDerre/TCC](https://github.com/EricDerre/TCC)), `Documentacao/memorial/2-pesquisa-e-literatura/`: `documentacao-como-contexto-rag.md` (§6.3), `quantizacao.md` (§6.4), `levantamento-2026-09-22-llms-locais.md` (§6.12.2 inferência em CPU, §6.12.3 RAG em corpus pequeno, §6.12.4 cache), com as referências originais (LEE et al. 2025; OUYANG et al. 2025; KAWRAKOW 2024; AKARSU; KARAMAN; MIERBACH 2026; WU; WU; ZOU 2024 – ClashEval; LIU et al. 2024 – Lost in the Middle).

Web (lidas em 23/10/2026):
- [Quesma — Do Qwen3.6 27B quantizations break the pelican? (jul/2026)](https://quesma.com/blog/qwen-quantization-quality/)
- [daily.dev — resumo de "Quantization hurts knowledge nonlinearly" (Quesma, ago/2026)](https://daily.dev/posts/quantization-hurts-knowledge-nonlinearly-1k1ale5qk)
- [llama.cpp — README do completion (`--load-mode`, mmap, mlock)](https://github.com/ggml-org/llama.cpp/blob/master/tools/completion/README.md)
- [Hugging Face — Welcome EmbeddingGemma](https://huggingface.co/blog/embeddinggemma)
- [Mem0 — documentação](https://docsearch.algolia.com/mcp/docs/repo/mem0ai/mem0) e [visão geral de ferramentas de memória 2026](https://futureagi.com/blog/best-llm-agent-memory-tools-2026/)
