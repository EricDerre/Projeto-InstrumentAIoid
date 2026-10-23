<!-- ! Alteração de IA - Revisar: arquivo criado em 23/10/2026 (pesquisa de hardware e modelos locais + benchmark medido nesta máquina).
     ! Motivo: o Eric pediu para medir a capacidade da máquina e achar modelos e otimizações que rodem junto com um jogo; os números da seção 8 saem dos scripts de bench/. -->
# Hardware e modelos locais — o que cabe no notebook do Eric (outubro de 2026)

Pesquisa feita em 23/10/2026 para o InstrumentAIoid. A pergunta: quais modelos e quais técnicas permitem rodar LLM com persona, voz (TTS + RVC), reconhecimento de fala, visão computacional jogando em tempo real e ferramentas como o Ultimate Vocal Remover **na mesma máquina, ao mesmo tempo que um jogo**.

Convenções: **[medido]** = número tirado nesta máquina (hoje ou nas fases do TCC); **[fonte]** = número publicado, com link no fim; **[estimativa]** = conta minha a partir de números medidos, foi conferida com as medições da seção 8, que valem mais que as estimativas.

---

## 1. A máquina (medida em 23/10/2026)

| Item | Valor |
|---|---|
| Modelo | Acer Nitro 5 AN515-45, Windows 11 Pro |
| CPU | AMD Ryzen 7 5800H — 8 núcleos / 16 threads (Zen 3), até ~4,4 GHz |
| GPU dedicada | NVIDIA GeForce GTX 1650 (notebook), **4 GB de VRAM**, Turing TU117 (compute 7.5), **sem Tensor Cores**, TGP 65 W, driver 617.14 |
| GPU integrada | Radeon Vega 8 (usa a RAM do sistema; 512 MB reservados) |
| RAM | 16 GB DDR4-3200 em dual channel (2×8 GB), ~15,4 GB utilizáveis |
| Disco | 2 NVMe de 1 TB (C: ~375 GB livres, D: ~159 GB livres) |
| Python | 3.14.4 no sistema |
| Uso de VRAM em repouso | **~825 MB** já ocupados (Wallpaper Engine, Firefox, Explorer, SourceTree, Área de Trabalho Remota) |

**Leitura rápida:** quem manda é a VRAM. Sobram ~3,2 GB de GPU antes de abrir qualquer jogo, e um jogo leve/médio em 1080p usa de 1,5 a 3,5 GB. Ou seja: **durante o jogo, a GPU é do jogo**. A IA precisa morar quase toda na CPU (que é boa: 8 núcleos Zen 3) e na RAM (apertada: o jogo + Windows levam 7–10 GB, sobrando ~5–7 GB para a IA).

Uma descoberta útil: as fases 2-A do TCC rodaram **nesta mesma máquina** (Ryzen 7 5800H, 15,4 GB, GTX 1650 presente e não usada, só CPU). Então já temos números reais de LLM em CPU aqui (seção 3).

---

## 2. Orçamento de recursos por modo de uso

A ideia central: o orquestrador (a "IA central") não deixa tudo carregado ao mesmo tempo. Ele troca de **modo** e carrega ou descarrega módulos conforme o modo.

| Modo | GPU (4 GB) | CPU (8c/16t) | RAM (16 GB) |
|---|---|---|---|
| **Jogando** | jogo (+ visão rápida, se couber) | LLM pequeno, STT, TTS, visão lenta | jogo 4–8 GB, IA ≤ 5 GB |
| **Conversando** (sem jogo) | LLM 3–4B inteiro na GPU, ou RVC | STT, TTS | IA ≤ 10 GB |
| **Estúdio** (cantar, separar stems) | RVC / UVR / síntese | resto | IA ≤ 10 GB |

Regras que saem daí:

1. **Um modelo pesado residente por vez na GPU.** Mesma regra que o TCC adotou para RAM, pelo mesmo motivo: o cache KV e os pesos são alocados inteiros no carregamento.
2. **Durante o jogo, LLM com `num_gpu: 0`** (só CPU). Partir o LLM entre CPU e GPU enquanto o jogo usa a GPU dá pior dos dois mundos: o jogo perde quadros e o LLM espera a GPU.
3. **Deixar 2 núcleos físicos livres para o jogo** (afinidade de CPU) e rodar a IA com prioridade "Abaixo do normal".
4. **Fechar ou pausar o Wallpaper Engine** no modo Jogando: ele já está ocupando GPU agora.
5. **Limitar o FPS do jogo** (por exemplo 60) para sobrar GPU, em vez de deixar o jogo usar 100%.

---

## 3. LLM com persona (o "cérebro" da assistente)

### 3.1 O que o TCC já mediu nesta máquina

Fase 2-A do TCC: Ollama 0.33.2, **só CPU**, Q4_K_M, `num_ctx=8192`, ~600 tokens de entrada **[medido]**:

| Modelo | RAM | Tempo por resposta (mediana) | Tokens de saída | Geração aproximada |
|---|---|---|---|---|
| `qwen2.5-coder:1.5b` | 1,3 GB | 5,2 s | 59–90 | ~14 tok/s **[estimativa]** |
| `qwen2.5-coder:3b` | 2,3 GB | 8,4–8,9 s | ~50 | ~8 tok/s **[estimativa]** |
| `phi4-mini:3.8b` | 3,5 GB | 9,8 s | ~41 | ~6 tok/s **[estimativa]** |
| `qwen2.5:7b` | 5,2 GB | 17,1–17,6 s | ~52 | ~4–5 tok/s **[estimativa]** |
| `granite4.2:8b` | 6,6 GB | 45,7 s | ~192 | ~4–5 tok/s **[estimativa]** |

O prefill (leitura do prompt) do `qwen2.5:7b` em CPU deu **~108 tokens/s** **[medido]**. A coluna "geração" é minha conta: tempo total menos o prefill, dividido pelos tokens de saída.

O que isso quer dizer para uma assistente que conversa: uma fala de 30–50 tokens com um modelo de 3–4B em CPU leva **~4–7 s**. Com 7B, ~10–15 s. Para conversa isso é lento, então é preciso **streaming**: mandar cada frase para o TTS assim que ela termina, em vez de esperar a resposta inteira.

### 3.2 Recomendação de modelo

| Situação | Modelo sugerido | Por quê |
|---|---|---|
| Jogando (CPU, pouca RAM) | `llama3.2:3b` (2,0 GB) ou `qwen3:4b-instruct` (2,5 GB); `ministral-3:3b` (3,0 GB, Apache 2.0, tool calling) é mais lento | cabem em ~3 GB de RAM; **medido: 9–11 tok/s em CPU com o jogo aberto** (seção 8.1) |
| Conversando sem jogo (GPU livre) | `llama3.2:3b` **inteiro na GPU** | **medido: 43 tok/s**; o 4B já não cabe inteiro (25 tok/s, dividido) |
| Qualidade máxima em português, sem pressa | `qwen2.5:7b` ou `qwen3:8b` partido CPU+GPU | o TCC mediu que abaixo de 5B o português perde mais (vão PT-EN de 5,1 pontos contra 4,3 em 7–8B) **[fonte: ALMEIDA et al., 2025, via TCC]** |
| Comandos/roteamento rápidos ("chama o módulo X") | `qwen3:1.7b` ou `qwen3:0.6b` com JSON forçado | só precisa escolher uma ferramenta, não conversar |

O `mistral` (7B, de 2024) que o `app/chat.py` usa hoje é o pior encaixe: é antigo, fraco em português, e não cabe na VRAM.

### 3.3 Ajustes que valem (lições do TCC)

Todas estas saem da pesquisa e das medições do TCC (`Documentacao/memorial/2-pesquisa-e-literatura/`):

- **Pesos em Q4_K_M.** Em CPU, Q8_0 deixa a geração ~2,27× mais lenta sem ganhar no prefill **[fonte: KAWRAKOW, 2024a]**. Não usar IQ4_XS em CPU: o prefill cai pela metade **[fonte]**.
- **Fixar `num_ctx`** (sugestão: 4096 para conversa). O TCC descobriu que **o Ollama descarta em silêncio o começo do prompt quando estoura o contexto** **[medido]**. Para uma persona isso é grave: o começo é justamente o prompt de sistema com a personalidade. O orquestrador tem que contar tokens e resumir o histórico antes de estourar.
- **Persona fixa no começo do prompt.** O cache de prefixo do Ollama funciona em CPU **[medido no TCC]**: se o prompt de sistema não muda, ele é processado uma vez só e as próximas falas pagam só o texto novo. Não coloque nada que muda (hora, estado do jogo) antes da persona; coloque depois.
- **Threads = núcleos físicos** (`num_thread: 6` no modo Jogando, 8 fora dele). Threads demais pioram a geração **[fonte: GGML-ORG, 2024]**.
- **Desligar o modo "thinking"** do Qwen3: multiplica os tokens de saída, que é exatamente o custo dominante em CPU **[fonte: YANG et al., 2025; medição do TCC]**.
- **Não quantizar o cache KV** em modelos pequenos (perde >5% de acurácia em 1,5B–7B) **[fonte: LIU et al., 2025]**, e no Ollama só funciona com flash attention, que vale só para algumas arquiteturas.
- **Saída estruturada (JSON Schema) para chamar módulos.** Decodificação restrita leva a validade do JSON a 100% em modelos de 0,6B–4B, com custo de 1,6–3,7% de vazão **[fonte: CHAVAN, 2026]**. Usar `/api/chat` com `format` (o `app/chat.py` usa `/api/generate`, sem histórico).
- **Memória da persona por recuperação (top-3), não "tudo no prompt".** O TCC mediu que a biblioteca recuperada sobe o acerto e a biblioteca inteira não **[medido]**, e que documentação errada é seguida em 93–96% dos casos: toda memória que a IA escreve sobre si mesma precisa de validação em código antes de entrar **[medido]**.
- **Gravar o digest do modelo** (`ollama show`): as tags do Ollama mudam sem aviso.

### 3.4 A GPU integrada (Vega 8): uma terceira via a testar

O Ollama tem backend Vulkan desde 0.12.11 (nov/2025), e GPUs integradas vêm **desligadas por padrão** porque podem ficar mais lentas que a CPU; liga-se com `OLLAMA_IGPU_ENABLE` **[fonte: webscraft, jun/2026]**. Na Vega 8 o modelo continua lendo da mesma RAM DDR4, então a geração dificilmente passa da CPU; o ganho possível é no prefill e em liberar núcleos da CPU para o jogo. **Vale um teste de 10 minutos**, não uma aposta.

O mesmo vale para a visão: a Vega 8 pode rodar o YOLO via ONNX Runtime DirectML, deixando a GTX 1650 inteira para o jogo (seção 6).

---

## 4. Voz: TTS + RVC (e canto)

### 4.1 Cadeia para a assistente falar

`texto do LLM → TTS base (CPU) → RVC com o modelo do Eric → áudio`

| Peça | Sugestão | Onde roda |
|---|---|---|
| TTS base | **Kokoro-82M** (tem vozes de português brasileiro) ou **Piper** `pt_BR` | CPU, bem mais rápido que tempo real |
| Conversão | **RVC** (modelo já treinado no Applio) | **GPU sempre** (medido: na CPU é mais lento que tempo real, seção 8.3) |

Pontos importantes:

- **O RVC roda em FP32 na GTX 1650.** O código oficial do RVC força precisão simples em placas da série 16 ("GTX 16-series cards use fp32"), porque o FP16 nelas dá NaN/áudio quebrado **[fonte: configs/config.py do RVC-WebUI]**. FP32 usa o dobro de VRAM e é mais lento. Conta com ~1,5–2,5 GB de VRAM para RVC em tempo real **[fonte: VoxBooster]**, que é exatamente o que o jogo não deixa sobrar.
- A GTX 1650 é citada como "mínimo viável, sem margem" para conversão de voz em tempo real **[fonte: VoxBooster]**.
- **A assistente não precisa de RVC em tempo real de microfone.** Ela fala frases que o LLM gerou. Então dá para converter **frase a frase** (por exemplo 2–4 s de áudio por vez) com uma latência de ~0,5–1,5 s, o que é aceitável. A medição (seção 8.3) mostrou que na CPU o RVC é mais lento que tempo real, então ele fica na GPU mesmo durante o jogo, ocupando ~1,3 GB.
- Para o pitch (f0): `rmvpe` é o melhor mas pesado; `fcpe` é mais leve e pensado para tempo real; em CPU, testar os dois.
- **Canto (Estúdio):** é offline. Renderiza a melodia (OpenUtau/DiffSinger, ver o relatório anterior) e passa o RVC por cima com GPU livre. Sem pressão de latência.

### 4.2 Reconhecimento de fala (o usuário falando com ela)

| Opção | Notas |
|---|---|
| **faster-whisper** `small` ou `base` em int8 na CPU | padrão maduro, bom português |
| **Parakeet TDT 0.6B v3** (NVIDIA, ONNX) | multilíngue (europeu, inclui português), substituiu o faster-whisper em servidores só de CPU **[fonte: letsdatascience, jul/2026]**; testar com sotaque brasileiro |
| **Silero VAD** na frente | só transcreve quando há fala, economiza CPU |

---

## 5. Ultimate Vocal Remover via Python

O caminho é o pacote **`audio-separator`** (MIT), que usa os mesmos modelos do UVR **[fonte: PyPI]**:

- Versão **0.47.1**, de 19/10/2026; Python ≥ 3.10 (exceto 3.14.1, então o 3.14.4 do Eric serve).
- Instalação: `pip install "audio-separator[gpu]"` (CUDA) ou `[cpu]`; `[dml]` para DirectML é experimental.
- Arquiteturas: MDX (`.onnx`), VR (`.pth`), Demucs, MDXC/RoFormer (`.ckpt`).
- Uso em Python: `Separator()` → `load_model("model_bs_roformer_ep_317_sdr_12.9755.ckpt")` → `separate("musica.wav")`. Na linha de comando: `audio-separator musica.wav --model_filename ...`.
- Os modelos baixam sozinhos na primeira vez; apontar `model_file_dir` para uma pasta dentro do projeto em vez da pasta temporária.

Na GTX 1650: separação é **trabalho de lote**, roda no modo Estúdio. Os modelos MDX-Net (ONNX) são os mais leves; os RoFormer dão a melhor qualidade mas são pesados em 4 GB e lentos em CPU **[estimativa: vários minutos por música em CPU; medir]**. Como é um script, encaixa direto como um módulo isolado ("separar stems") que a IA central chama.

---

## 6. Visão computacional jogando em tempo real

### 6.1 A arquitetura que cabe: reflexo rápido + pensamento lento

Um LLM ou VLM **não consegue** jogar em tempo real nesta máquina: um VLM pequeno leva segundos por imagem em CPU. Mesmo a Neuro-sama não joga osu! com o LLM: usa um modelo próprio para o jogo, e o LLM só comenta. O desenho que funciona aqui tem duas camadas:

| Camada | O que faz | Frequência | Modelo | Onde roda |
|---|---|---|---|---|
| **Reflexo** | vê a tela e aperta botões | 20–60 vezes por segundo | detector pequeno (YOLO) + regras ou uma política pequena treinada | Vega 8 (DirectML), CPU ou GPU com folga |
| **Pensamento** | entende a situação, decide estratégia, comenta | a cada 2–10 s | VLM pequeno ou LLM recebendo o estado em texto | CPU |

A camada lenta manda objetivos ("vai para a esquerda", "foge") para a rápida, que executa. É o que permite jogar "como um humano olhando a tela", sem ler a memória do jogo.

### 6.2 Peças

- **Captura de tela:** `dxcam` / `bettercam` (Desktop Duplication do Windows), que capturam centenas de quadros por segundo com pouco custo. Recortar a região que importa e reduzir para 320–416 px antes do modelo.
- **Detector:** **YOLO26n** (2,4 M parâmetros, 40,9 mAP, **38,9 ms em CPU via ONNX a 640 px**) ou YOLO11n (56,1 ms) **[fonte: Ultralytics]**. Em 320 px o custo cai para cerca de 1/4 **[estimativa]**, ou seja ~10 ms em CPU: **dá para rodar o reflexo sem tocar na GTX 1650**. Treinar com prints do próprio jogo rotulados (algumas centenas de imagens bastam para começar).
- **Política:** começar com regras (máquina de estados em cima das detecções). Depois, clonagem de comportamento: gravar o Eric jogando (tela + teclas) e treinar uma CNN pequena para imitar.
- **Referência de ponta:** **NVIDIA NitroGen** (jan/2026), 493 M parâmetros (SigLIP2 + DiT), recebe quadros 256×256 e devolve ações de controle, treinado em mais de 1.000 jogos **[fonte: Hugging Face]**. Licença **não comercial**, e a NVIDIA não publicou requisitos de inferência. Serve de estudo e de inspiração para a camada reflexa; em 4 GB FP32 é arriscado junto com um jogo.
- **Camada lenta:** VLMs pequenos de 2025–2026: SmolVLM2 (256M/500M/2.2B, Apache 2.0), Qwen3-VL 2B/4B (Apache 2.0), Gemma 3n/4 E2B, LFM2.5-VL 450M, Moondream **[fonte: aiidelist]**. Nenhum publica latência comparável; medir nesta máquina. Alternativa mais barata: passar para o LLM o **estado em texto** que o YOLO já extraiu ("3 inimigos à direita, vida 40%") em vez da imagem.
- **Entrada:** `pydirectinput` (teclado/mouse que jogos aceitam) ou `vgamepad` (controle virtual de Xbox).

### 6.3 Escolha de jogos para começar

Jogos 2D, leves e com pouca informação na tela (ritmo, plataforma simples, puzzle, tower defense) deixam GPU sobrando e precisam de pouca visão. Jogos 3D rápidos são a última etapa.

---

## 7. Agendamento entre jogo e IA (como não travar tudo)

O Windows não tem um "MPS" da NVIDIA para dividir a GPU entre processos, então a divisão é feita pelo orquestrador:

1. **Modos com carga e descarga explícitas** (seção 2). No Ollama: `OLLAMA_MAX_LOADED_MODELS=1`, `OLLAMA_NUM_PARALLEL=1`, e `keep_alive: 0` para descarregar na troca de modo.
2. **Medir a VRAM livre antes de carregar** algo na GPU (biblioteca `pynvml`). Se não couber, usar a versão CPU do módulo.
3. **Prioridade e afinidade de processo** (`psutil`): IA em "Abaixo do normal", com os núcleos 0–3 deixados para o jogo, por exemplo.
4. **Fila única de GPU** no orquestrador: RVC, UVR e LLM-na-GPU nunca rodam ao mesmo tempo; um pedido espera o outro.
5. **Configurações do Windows:** em Configurações → Sistema → Tela → Gráficos, marcar o jogo como "Alto desempenho" (GTX 1650) e os processos auxiliares como "Economia de energia" (Vega 8). O "Agendamento de GPU acelerado por hardware" pode ser testado ligado e desligado; o efeito varia.
6. **Ambientes Python separados por módulo** (com `uv`): o RVC/Applio e o DiffSinger pedem Python 3.10–3.11, enquanto o app e o `audio-separator` rodam no 3.12+. Cada módulo como processo próprio com uma API local (FastAPI ou socket) casa com a arquitetura de módulos isolados e evita conflito de dependências.
7. **Notebook na tomada e em modo desempenho** (NitroSense): na bateria a GPU e a CPU caem bastante de potência.

---

## 8. Resultados medidos (23/10/2026)

Medido nesta máquina com os scripts de `bench/` (rodar de novo com `bench\rodar_tudo.ps1 <cenario>`). Dois cenários: **sem jogo** (só o desktop, ~825 MB de VRAM ocupados) e **com Warcraft III aberto** (GPU a 95–98% de uso, ~1,7 GB de VRAM, ~49 W, 59 °C, e só ~1 GB de RAM livre no início). Estes números substituem as estimativas das seções 3 a 6.

### 8.1 LLM (Ollama 0.40.8, Q4_K_M, `num_ctx` 4096, resposta de até 80 tokens, persona da Astolfo)

| Modelo | Onde | Geração sem jogo | Geração com jogo | Resposta (mediana) sem / com jogo |
|---|---|---|---|---|
| `qwen3:1.7b` | CPU | 19,4 tok/s | 17,8 tok/s | 5,2 s / 5,0 s |
| `qwen3:1.7b` | GPU | **91,3 tok/s** | 15,9 tok/s | 2,7 s / 5,4 s |
| `llama3.2:3b` | CPU | 12,4 tok/s | 11,2 tok/s | 6,0 s / 5,2 s |
| `llama3.2:3b` | GPU | 42,7 tok/s | 13,1 tok/s | 3,4 s / 5,9 s |
| `qwen3:4b-instruct` | CPU | 11,7 tok/s | 8,9 tok/s | 6,6 s / 9,2 s |
| `qwen3:4b-instruct` | GPU (66% na GPU) | 25,4 tok/s | 19,1 tok/s | 4,4 s / 6,0 s |
| `ministral-3:3b` | CPU / GPU parcial | 10,3 / 19,9 tok/s | não medido | 9,1 s / 5,7 s (sem jogo) |
| `qwen2.5:7b` | CPU / GPU parcial | 6,3 / 11,4 tok/s | não medido | 8,4 s / 5,8 s (sem jogo) |
| `qwen3-8b-heretic` | CPU / GPU parcial | 5,8 / 8,5 tok/s | não medido | 16,3 s / 12,2 s (sem jogo) |

O prefill (leitura do prompt) ficou entre 180 e 570 tok/s em CPU. O que os números dizem:

- **Com o jogo aberto, a GPU deixa de ajudar o LLM.** O `qwen3:1.7b` cai de 91 para 16 tok/s na GPU, pior que na CPU (18 tok/s). A CPU quase não sente o jogo (perde 5–25%). Isso confirma a regra da seção 2: no modo Jogando, LLM com `num_gpu: 0`.
- **Só cabem ~2,2 GB de modelo na GPU** mesmo sem jogo. De 4B para cima o Ollama divide o modelo entre GPU e CPU.
- **Cuidado com o `qwen3:4b` padrão:** ele ignora `think: false` e escreve o raciocínio em inglês na resposta. Usar a tag **`qwen3:4b-instruct`**, que respondeu direto e em português. O `qwen3-8b-heretic` tem o mesmo problema (`<think>` na resposta).
- **Escolha para o modo Jogando:** `llama3.2:3b` ou `qwen3:4b-instruct` na CPU (~9–11 tok/s: uma fala de 40 tokens em ~4–5 s). O `qwen3:1.7b` é o mais rápido, mas inventa mais ("cantar canções enquanto fazia um coelho").

### 8.2 Voz (CPU, frase de teste com 6,4 s de fala)

| Peça | Sem jogo | Com jogo |
|---|---|---|
| Piper `pt_BR-faber-medium` | 0,27 s (RTF 0,04) | 0,42 s (RTF 0,06) |
| Kokoro `pf_dora` / `pm_alex` (pt-br) | 2,2 s (RTF 0,34) | 2,7 s (RTF 0,43) |
| faster-whisper `base` int8 | 0,83 s | 1,0 s, mas errou "Astolfo" → "Astofo" |
| faster-whisper `small` int8 | 2,1 s, transcrição perfeita | 2,9 s, transcrição perfeita |

Tudo isso roda bem mais rápido que tempo real na CPU, mesmo com o jogo. O Kokoro precisa de `ONNX_PROVIDER=CPUExecutionProvider` quando o `onnxruntime-directml` está instalado (no DirectML ele quebra).

### 8.3 RVC com o modelo astolfoV3 (motor do Applio, mesma frase de 6,4 s)

| Onde | f0 | Sem jogo | Com jogo |
|---|---|---|---|
| GPU (FP32) | rmvpe | **0,86 s** (RTF 0,13) | 3,45 s (RTF 0,54) |
| GPU (FP32) | fcpe | **0,76 s** (RTF 0,12) | 3,08 s (RTF 0,48) |
| CPU | rmvpe | 7,6 s (RTF 1,19) | 9,9 s (RTF 1,55) |
| CPU | fcpe | 7,4 s (RTF 1,15) | 9,3 s (RTF 1,45) |

- O RVC usa **~1,3 GB de VRAM** (pico do PyTorch) e a primeira conversão leva ~45 s (carregar o modelo e o rmvpe). Ele precisa ficar carregado o tempo todo.
- **Na CPU o RVC é mais lento que tempo real**, então durante o jogo ele precisa da GPU. Com o jogo aberto ele ainda converte mais rápido que tempo real (RTF ~0,5), o que basta para falar frase a frase com ~1,5–3 s de atraso.
- O `fcpe` é um pouco mais rápido que o `rmvpe` e gasta menos na primeira carga. Falta ouvir os dois e comparar a qualidade.
- **Orçamento real de VRAM no modo Jogando:** jogo (~1,7 GB no Warcraft III) + desktop + RVC (~1,3 GB) ≈ 3,8 GB dos 4 GB. Não sobra espaço para LLM nem para visão na GTX 1650.

### 8.4 Visão (captura de tela e YOLO26n)

| Peça | Sem jogo | Com jogo |
|---|---|---|
| Captura `dxcam` 1080p | 120 quadros/s (o máximo pedido) | 120 quadros/s |
| YOLO26n 320 px, CPU (ONNX) | 8,8 ms | 12,4 ms |
| YOLO26n 320 px, **Radeon integrada** (DirectML) | 6,2 ms | **10,2 ms** |
| YOLO26n 320 px, GTX 1650 (DirectML) | 4,6 ms | 18,6 ms |
| YOLO26n 320 px, GTX 1650 (PyTorch/CUDA, com pré e pós-processamento) | 16,4 ms | 48,0 ms |
| YOLO26n 640 px, CPU / Radeon / GTX (DirectML) | 36 / 25 / 12,9 ms | 52,6 / **28,3** / 41,9 ms |

- **Com o jogo aberto, a Radeon integrada é o melhor lugar para a visão:** 10 ms em 320 px (até ~100 detecções por segundo) sem tirar nada da GTX 1650. A GTX, disputada com o jogo, fica quase 2× mais lenta que a integrada.
- A captura de tela não é gargalo.
- No DirectML, o dispositivo 0 é a Radeon e o 1 é a GTX 1650.

### 8.5 Como fica o modo Jogando, com base nas medições

| Módulo | Onde roda | Custo medido com o jogo |
|---|---|---|
| Jogo | GTX 1650 | ~1,7 GB de VRAM, 95–98% de uso (Warcraft III) |
| Visão rápida (YOLO26n 320 px) | Radeon integrada (DirectML) | ~10 ms por quadro |
| LLM (`llama3.2:3b` ou `qwen3:4b-instruct`) | CPU | 9–11 tok/s, ~2,5–3 GB de RAM |
| TTS (Piper; Kokoro se a voz for melhor) | CPU | 0,4–2,7 s por frase de 6 s |
| RVC astolfoV3 | GTX 1650 | ~1,3 GB de VRAM, RTF ~0,5 |
| STT (`small` int8) | CPU | ~3 s para 6 s de fala |

Dois limites apareceram que não estavam previstos. O primeiro é a **RAM**: com o Warcraft III e os programas abertos sobrava só ~1 GB livre, então LLM (~3 GB) + Whisper + Kokoro + RVC vão forçar o Windows a usar o disco. Fechar programas no modo Jogando (navegador, Teams, Discord, Wallpaper Engine) é obrigatório, e o primeiro upgrade de hardware que mais ajuda é **mais RAM** (32 GB). O segundo é que **a GPU fica no limite** com jogo + RVC, então qualquer outra coisa na GTX (LLM, VLM) está fora no modo Jogando.

Ainda falta medir:

- a queda de FPS do jogo quando cada módulo está rodando (só medi o lado da IA);
- a qualidade do RVC com `fcpe` × `rmvpe`, ouvindo os arquivos em `bench/audio/`;
- o RVC em ONNX (o Applio tem `inference_engine` ONNX), que pode ser mais leve;
- um VLM pequeno na CPU para a camada lenta da visão.

---

## Fontes

Desta máquina e do TCC:
- Medição de hardware: PowerShell `Win32_*` e `nvidia-smi` no dispositivo do Eric, 23/10/2026.
- TCC, Fase 2-A (só CPU no Ryzen 7 5800H): `Documentacao/memorial/3-resultados-e-analises/fase-2a-relatorio-por-modelo.md` e `Programacao/AgenteCore/experimentos/resultado_benchmark.md` — [github.com/EricDerre/TCC](https://github.com/EricDerre/TCC)
- TCC, pesquisa: `quantizacao.md`, `medicao-em-cpu-e-estatistica.md`, `modelos-locais-e-portugues.md`, `memoria-gerida-pelo-modelo.md` e `levantamento-2026-09-22-llms-locais.md` (§6.12.2 inferência em CPU; §6.12.5 modelos pequenos e português), com as referências originais (KAWRAKOW 2024a/b, GGML-ORG 2024, LIU et al. 2025, ALMEIDA et al. 2025, YANG et al. 2025, CHAVAN 2026, OLLAMA 2025/2026).
- Relatório anterior deste projeto: `docs/pesquisa/notas-detalhadas-en/caminho-tecnico-do-projeto.md` (§4–5: Python 3.14, PyTorch na GTX 1650, modelos do Ollama que cabem em 4 GB).

Web (lidas em 23/10/2026):
- RVC força FP32 na série GTX 16: [RVC-WebUI configs/config.py](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/blob/main/configs/config.py)
- VRAM e latência de conversão de voz, GTX 1650 "mínimo viável": [VoxBooster — Voice Changer GPU Acceleration Explained](https://voxbooster.com/blog/voice-changer-gpu-acceleration-explained)
- audio-separator 0.47.1: [PyPI audio-separator](https://pypi.org/project/audio-separator/)
- YOLO26 × YOLO11: [Ultralytics — YOLO11 vs YOLO26](https://docs.ultralytics.com/compare/yolo11-vs-yolo26)
- Parakeet × Whisper em CPU: [letsdatascience, jul/2026](https://letsdatascience.com/news/parakeet-outperforms-whisper-on-low-cost-cpu-deployment-de238707)
- NitroGen: [ficha do modelo (espelho de nvidia/NitroGen)](https://huggingface.co/aoiandroid/NitroGen), [The Decoder](https://the-decoder.com/nvidia-wants-to-create-universal-ai-agents-for-all-worlds-with-nitrogen/)
- VLMs pequenos: [aiidelist — on-device VLM comparison](https://aiidelist.com/blog/on-device-vlm-comparison.md)
- Ollama Vulkan e iGPU: [webscraft — Ollama 0.30](https://webscraft.org/blog/ollama-030-scho-novogo-gguf-vulkan-llamacpp-i-tool-calling?lang=en)
- Kokoro (vozes por idioma): [tts.ai/voices/kokoro](https://tts.ai/voices/kokoro/)
- Agendamento de GPU no Windows 11: [PCWorld](https://www.pcworld.com/article/2339130/should-you-enable-hardware-accelerated-gpu-scheduling-in-windows-11.html)
