# Expressive score/MIDI-driven instrument synthesis ("a VOCALOID for instruments"): state of the art as of 8 October 2026

Research date: 2026-10-08. Local copies of GitHub READMEs/LICENSE files were used as reference data and cross-checked online where possible. GitHub's API and Hugging Face's API were blocked from the sandbox, so repository activity comes from README text, GitHub pages fetched one by one, and PyPI release dates. Companion notes for singing products are in `../Apps de vocaloid e integrações/apps_comerciais_e_vozes_famosas.md`.

## 1. Commercial products that do "VOCALOID-like" instruments, AI instrument rendering, physical modelling or timbre transfer

### Takeaway
"VOCALOID for instruments" now exists as a commercial category, and two of the main singing-synth vendors built it on their vocal editors. Dreamtonics' Instrument X (launched 26 August 2026) turns notation into performances with neural acoustic models of orchestral instruments. It runs locally with no GPU and costs US$99 per instrument. ACE Studio 2.0 (December 2025) offers 40+ MIDI-driven AI instruments but renders them in the cloud. Physical modelling (SWAM, Sample Modeling) is still the lightweight real-time benchmark, at about US$99 to US$159 per instrument. Voice- or sound-to-instrument tools (Kits.ai, Neutone Morpho, Combobulator, SoundID VoiceAI) are driven by audio rather than by a score. Yamaha has shown AI wind-instrument synthesis (2021) but sells no product.

### Cited Findings

#### Score/MIDI-driven AI instruments (closest to the InstrumentAIoid idea)
- **Dreamtonics Instrument X:** announced 26 Aug 2026 as "the newest addition to the Dreamtonics ecosystem", next to Synthesizer V Studio 2 Pro and Vocoflex. Dreamtonics describes it as "neural acoustic modeling" that replaces static sample libraries and turns notation into performances. It runs entirely on the local machine, with no dedicated GPU or internet connection — [Dreamtonics: Instrument X First Look](https://dreamtonics.com/?p=4621); release also reported 27 Aug 2026 — [Sonicstate](https://sonicstate.com/news/2026/08/27/dreamtonics-releases-instrument-x-/)
- **Instrument X editing model:**
  - Unified Articulation Editor: "Smart Articulation" is automatic, or you can control articulations per note. Staccato, legato, tenuto, col legno and brass mutes can be stacked on one note.
  - Dynamics Lane: dynamics are set automatically from pitch, duration and phrasing, with manual override. Changing dynamics also changes timbre, harmonic saturation and response, not only gain.
  - "AI Performance Retakes": regenerate a whole section, or target timbre drift, micro-pitch curves or intensity.
  - Polyphony: overlapping notes are rendered as separate voices.
  - Microphone Mixer: spot mics, Decca tree and room pairs.
  - Five style presets per instrument: Adagio, Allegro, con Fuoco, Pop and Ballade.
  - Dreamtonics says it "inherits the elite workspace DNA of Synthesizer V".
  — [Dreamtonics](https://dreamtonics.com/?p=4621)
- **Instrument X line-up:** the article says there are 15 expansions at launch but names only these: Violin 1, Viola 1, Violoncello 1, Contrabass 1, Flute 1, Piccolo 1, Oboe 1, Clarinet in A 1, Bassoon 1, Trumpet 1, Trombone 1, Horn 1 and Tuba 1 — [Dreamtonics](https://dreamtonics.com/?p=4621). A second source describes the launch line-up as strings, winds, brass and saxophones — [Magnetic Mag](https://magneticmag.com/2026/09/dreamtonics-shows-how-instrument-x-was-built/)
- **Instrument X technical details:**
  - Formats: VST3, AU and AAX on Windows and macOS.
  - Up to 11 concurrent microphone feeds.
  - A patent-pending algorithm measures the studio's acoustics with a custom dodecahedral speaker array, to separate the room from the dry instrument.
  - Runs on a standard laptop without a dedicated GPU.
  — [Rekkerd](https://rekkerd.org/dreamtonics-launches-instrument-x-neural-acoustics-modeling-engine/)
- **Instrument X approach and price:** described as "a neural acoustics modeling engine rather than a sample player". It models legato, breath swells, room behaviour, instrument response and mic perspective as one system. Pricing: the host engine is free; expansions cost US$99 each; Orchestral Essentials US$349; Complete Collection US$649; 14-day trial — [Magnetic Mag](https://magneticmag.com/2026/09/dreamtonics-shows-how-instrument-x-was-built/)
- **Instrument X update:** a 1.0.2 update was posted on 6 Oct 2026 — [Dreamtonics news](https://dreamtonics.com/news/). This comes from the companion notes file and was not re-checked here.
- **ACE Studio 2.0 (Timedomain), release:**
  - Released 8 Dec 2025, with new "artist-made AI instruments" covering violins, violas, cellos, saxophones, trumpet and duduk.
  - The saxophones are credited to Bob Magnuson and Carlo Alfonso, the trumpet to Xiaochuan Li.
  - The AI instruments generate parts from MIDI data.
  - Prices: Artist US$398, Artist Pro US$528. Requires Windows 10+ or macOS 13+.
  — [Recording Magazine](https://www.recordingmag.com/news/ace-studio-2-0-all-in-one-ai-music-studio-released/)
- **ACE Studio official site:**
  - "Generate natural-sounding instrument performances with only MIDI, while retaining full control".
  - Ensemble Mode layers several AI instruments on one track.
  - "AI String Sections" (Violins 1/2, Violas, Celli, Basses) were recorded with the Budapest Art Orchestra.
  - The ACE Bridge plug-in (VST3/AU/AAX) triggers instruments from MIDI, with parameter automation and ARA tempo sync.
  - The FAQ says AI rendering needs internet because "the AI services operate in the cloud".
  - Instrument output is royalty-free for commercial use.
  - The models are trained with professional instrumentalists, who receive royalty shares based on usage.
  — [ACE Studio](https://acestudio.ai/)
- **ACE Studio pricing:** 40+ royalty-free AI instruments in both Artist (US$16.58/month billed yearly, 2,500 credits/month) and Artist Pro (US$22/month, 5,000 credits/month); 7-day money-back guarantee — [ACE Studio pricing](https://acestudio.ai/pricing/)
- **Sound On Sound review of ACE Studio 2 (March 2026):**
  - The initial instruments are violin, cello, trumpet and saxophone, "focused on non-chordal options".
  - Expression comes from voicebanks built from real performers.
  - A "smart" mode assigns articulations automatically.
  - Basic real-time preview sounds help you record the MIDI before rendering.
  - The reviewer got "very usable performances" from strings and brass by scratch-singing a part, converting it with Vocal-to-MIDI, then assigning an AI instrument.
  - Limitations noted: no chordal instruments, and no third-party plug-ins in the Canvas.
  - UK prices including VAT: Artist US$497, Artist Pro US$660 one-off. These differ from the US$398/US$528 in the US press release.
  — [Sound On Sound](https://soundonsound.com/reviews/ace-studio-2)
- **ACE Studio and EastWest:** a strategic partnership announced 27 Jan 2026 combines EastWest libraries with ACE's AI performance technology. ACE's instruments are controlled through MIDI and performance data for phrasing, articulation and expression. No products, dates or prices were announced — [Sound On Sound](https://www.soundonsound.com/news/ace-studio-and-eastwest-sounds-partnership)
- **Yamaha "AI Sound Synthesis Technology" (announced 2021):**
  - Performs wind instruments (saxophones, trumpets, flutes, clarinets, oboes) from a note score.
  - Infers vibrato, crescendo and decrescendo from the notes.
  - Learns a performer's timbre, style and timing from recordings, with a dynamics parameter and a song ID as extra inputs.
  - Reads the whole score first, then generates the sound frame by frame (for example 100 times per second).
  - Real-time expression control was shown at the "AI Artist Stage" exhibit (June 2021, Hamamatsu; now ended).
  - It is the sibling of VOCALOID:AI (2019). The page does not say it is commercially available.
  — [Yamaha R&D](https://www.yamaha.com/en/tech-design/research/technologies/aisynth/)
- **Yamaha "AI Performance Expression Rendering":** a deep neural network that adds human-like key timing and velocity to piano scores. It can imitate a specific performer, and was used in the "Dear Glenn" project (Ars Electronica 2019). No product or API is named — [Yamaha R&D](https://www.yamaha.com/en/tech-design/research/technologies/performance_rendering)

#### Physical-modelling and phrase-modelling benchmarks (non-neural)
- **SWAM Viola v3 (Audio Modeling):**
  - Price about US$99, with a 15-day trial.
  - Physical model of bow–string interaction: bow speed, pressure and position shape the sound in real time. No sample playback is described.
  - Install size 36–84 MB on Windows, 52–180 MB on macOS. About 52 MB RAM per instance. Minimum CPU: 1.6 GHz Core 2 Duo.
  - Formats: Standalone, VST, VST3, AAX, plus AU on macOS; NKS.
  - Platforms: macOS 10.13–27 and Windows 10/11.
  — [Audio Modeling](https://audiomodeling.com/strings/swam-viola)
- **PolySWAM (ILIO + Audio Modeling):** announced 19 Aug 2026. A polyphonic orchestral instrument on the SWAM engine, with voice allocation that spreads notes across virtual players. Preorder US$279 (from 13 Aug), regular US$399, release expected mid-September 2026. The existing SWAM instruments are "monophonic by design" — [Sonicstate](https://sonicstate.com/news/2026/08/19/polyswam-expressive-polyphonic-orchestral-instrument/)
- **Sample Modeling:**
  - Prices: Solo Strings €299; Solo, Chamber & Ensemble Strings €449; Brass Bundle v3 €399; The Trumpet v3 €159; Complete Bundle €699.
  - "Harmonic Alignment" gives continuous dynamics. Articulations come from velocity, expression, pitch wheel, mod wheel and MIDI CCs.
  - The Trumpet was first released in 2008; the strings in 2017. The site was last modified 2025-02-07.
  - A headline reads "A new chapter for Native Instruments, Kontakt and Samplemodeling", with no details.
  — [Sample Modeling](https://www.samplemodeling.com/)
- **Synful Orchestra:**
  - "Now Completely Free of Charge".
  - Patented Reconstructive Phrase Modeling: recorded phrase fragments are spliced and resynthesised with additive synthesis.
  - Native 64-bit on macOS (Intel and Apple Silicon) and Windows; AU/VST3/AAX.
  - Donation appeal: "Please Help Synful Orchestra Survive". No last-update date is given.
  — [Synful](http://www.synful.com/)
  - Made free in August 2023 — [Synthtopia](https://www.synthtopia.com/?p=138656)

#### Audio-driven conversion (voice or sound to instrument), not score-driven
- **Kits.ai:** voice-to-instrument models turn a hum, beatbox, whisper or guitar note into an instrument sound — [Kits.ai blog, 21 Aug 2023](https://kits.ai/blog/ai-instruments-on-kits). The help article (19 Aug 2026) describes choosing an instrument and converting uploaded or recorded audio "in minutes". It lists no instrument names or prices — [Kits.ai Help](https://help.kits.ai/hc/en-us/articles/25540107397395-How-do-I-use-AI-Instrument-Models-on-Kits-AI)
- **Neutone Morpho:**
  - Real-time "tone morphing" plug-in (examples: voice to violin, objects to drums).
  - V1 released 26 Apr 2024. Free with 4 models; a US$99 upgrade adds 10 more; 15+ more models in the store. A cloud custom-training service ("Neutone Cocoon") was announced.
  — [Sonicstate](https://sonicstate.com/news/2024/04/26/neutone-morpho-v1-released/)
  - Manual for v1.1.4 (24 Jun 2026): VST3/AU on macOS, VST3 on Windows 10/11. It is driven by audio "rather than traditional MIDI information". Custom models via an online training service.
  — [Morpho manual](https://neutone.supabase.co/storage/v1/object/public/morpho-public/manual/2026-06-25_NeutoneMorpho_Manual.pdf)
- **DataMind Audio Combobulator:**
  - V1.0 released September 2024. Neural audio synthesis for timbral style transfer through artist "Brains".
  - Artists receive 50% of profits from their Brain's sales.
  - Each Brain has a low-latency real-time version. No internet connection or subscription needed.
  — [Sonicstate](https://sonicstate.com/news/2024/09/06/neural-audio-synthesis-for-your-daw/)
  - US$99, AU/VST, three Brains included — [DataMind Audio](https://datamindaudio.ai/)
- **Sonarworks SoundID VoiceAI:** "over 50 royalty-free voice and instrument presets" (examples: drums, guitars, violins from humming or beatboxing). Processing can be unlimited and local, or in the cloud — [Sonarworks blog, 29 Apr 2025](https://www.sonarworks.com/blog/learn/can-you-turn-your-voice-into-an-instrument)
- **Sonic Charge Synplant 2 "Genopatch":** AI that analyses an imported sample and builds a matching patch for Synplant's own synth engine (no sampling). It gets close on synth sources and is less accurate on acoustic sources. €149/US$149; reviewed 8 Dec 2023 — [MusicRadar](https://www.musicradar.com/reviews/sonic-charge-synplant-2-review)
- **Dreamtonics Vocoflex:** real-time voice-morphing plug-in, US$199, aimed at voices — [Dreamtonics Vocoflex](https://dreamtonics.com/vocoflex/) (from the companion notes)

#### Other notable 2024–2026 events
- Google's Magenta RealTime 2 (4 Jun 2026) adds MIDI note control to an open-weights streaming music model; see §2 — [Magenta](https://magenta.withgoogle.com/magenta-realtime-2)
- Google's DDSP-VST plug-in repository was archived on 9 Oct 2024 — [GitHub](https://github.com/magenta/ddsp-vst/releases)

### Inferences
- **Shared voice/instrument infrastructure is proven.** Both leading AI singing vendors extended their singing editors to instruments: Instrument X "inherits" Synthesizer V's workspace, and ACE puts AI instruments in the same piano roll. Yamaha's wind synthesis is the sibling of VOCALOID:AI. This supports InstrumentAIoid's plan of one score editor with neural renderers for both voices and instruments.
- **The feature bar users now expect:**
  - automatic plus per-note articulations, including legato transitions;
  - one dynamics/intensity lane that changes timbre, not only volume;
  - phrase-level regeneration ("retakes") and style presets;
  - mic/room simulation.
- **Two deployment models exist.** Instrument X shows local, CPU-only neural rendering is commercially viable; ACE uses cloud rendering with credits.
- **Price anchors:** about US$99 per instrument (Instrument X, SWAM viola), US$99 for Combobulator and for the Morpho upgrade.
- **Every vendor started with monophonic sustained instruments** (strings, winds, brass). Chordal instruments lag: ACE is "non-chordal", and SWAM was monophonic until PolySWAM.
- **A reusable workflow.** The reviewer's "scratch-sing, then audio-to-MIDI, then AI instrument" path suggests InstrumentAIoid can reuse its vocal input pipeline (pitch tracking or transcription) to drive instruments.

### Gaps
- **Instrument X unknowns:** model architecture, training data, system requirements (CPU/RAM/disk), MIDI import, real-time playback versus offline rendering, and the names of all 15 expansions. The official product page returned no content, and the MusicRadar URL was too long to fetch.
- **ACE Studio unknowns:** the full list of 40+ instruments, per-instrument parameters, how credits are consumed, and whether any instrument rendering is local.
- **Smaller products:** Kits.ai instrument list and prices, Combobulator system requirements, SWAM prices beyond the viola, what Sample Modeling's NI/Kontakt announcement means, and Synful's last update date.
- **No independent listening tests** comparing Instrument X, ACE instruments, SWAM and Sample Modeling were found.

## 2. Open-source and academic work (DDSP, RAVE, Neutone, Magenta RT, diffusion and score-to-audio, SVS stacks, vocoders, voice conversion)

### Takeaway
Open, controllable instrument synthesis still revolves around DDSP: pitch and loudness drive a harmonic-plus-noise synthesizer. These models are tiny, run in real time on a CPU, and use Apache or MIT licences. But Google's TensorFlow code is frozen (DDSP-VST and MIDI-DDSP are archived). The maintained descendants live in the singing-voice community: pc-ddsp (updated 28 Sep 2026), DDSP-SVC, and OpenVPI's DiffSinger and SingingVocoders.

RAVE and BRAVE give strong low-latency timbre transfer but are CC BY-NC, so they cannot be used commercially. Large generative models (Magenta RT 2, Stable Audio Open, ACE-Step 1.5) are not precise MIDI renderers. Magenta RT 2 is the first open model with MIDI note control, but it runs in real time only on Apple Silicon.

Score-to-audio research quality is improving: Deep Performer, MIDI-DDSP, spectrogram diffusion, guitar diffusion outpainting, CoSaRef, TokenSynth and MIDI-VALLE. Maintained, permissively licensed code is rare.

### Cited Findings

#### Quick-reference table (details and sources in the bullets below)
| Project | What it does | Licence | Status / last activity | Real-time |
|---|---|---|---|---|
| magenta/ddsp | Differentiable DSP library (TensorFlow) | Apache-2.0 | Not archived; last PyPI release 3.7.0, 25 May 2023 | Yes (small models) |
| DDSP-VST | DDSP synth and effect plug-ins (JUCE + TFLite) | Apache-2.0 | Archived 9 Oct 2024 | Yes |
| MIDI-DDSP | MIDI → expression → DDSP, 13 URMP instruments | Apache-2.0 | Archived 1 Feb 2024; PyPI 0.2.6, 30 Nov 2022 | No (offline) |
| ddsp-piano | MIDI → piano (TF DDSP) | Apache-2.0 | DAFx 2022 / JAES 2023; last commit unknown | Offline |
| acids-ircam ddsp_pytorch | f0 + loudness → audio; Pd external | Apache-2.0 | Date unknown | Yes (CPU) |
| DDX7 | Differentiable FM synthesis | Apache-2.0 | ISMIR 2022 | n/a |
| pc-ddsp | DDSP vocoders (Sins / CombSub) | MIT | Updated 28 Sep 2026 | n/a |
| SawSing | DDSP singing vocoders | **AGPL-3.0** | ISMIR 2022 | n/a |
| RAVE / nn~ / rave_vst / BRAVE | Audio VAEs; timbre transfer | **CC BY-NC 4.0** (no commercial use) | RAVE PyPI 2.3.1 (Dec 2023); nn~ 1.6.0 (May 2025); rave_vst archived; BRAVE (JAES 2025) | Yes |
| Neutone SDK | Wraps PyTorch models for DAW host plug-ins | LGPL-2.1 | v1.5.2, 13 Nov 2025 | FX yes / Gen no |
| music-spectrogram-diffusion | Multi-instrument MIDI → spectrogram → audio | Apache-2.0 | Archived 6 Jan 2026 | No |
| Magenta RT 2 | Streaming music LM with text, audio and MIDI control | Apache-2.0 code; CC-BY 4.0 weights | 4 Jun 2026; PyPI 2.0.3, 30 Jul 2026 | Apple Silicon only |
| Stable Audio Open 1.0 / Small + stable-audio-tools | Text → audio | Stability Community License (code: MIT) | Tools 0.0.20, 20 May 2026 | Small model optimised for Arm CPUs |
| ACE-Step v1 / 1.5 | Text/lyrics → song; cover, repaint, stems | Apache-2.0 (v1) / MIT (1.5) | 1.5 XL released 2 Apr 2026 | No (fast offline) |
| TokenSynth | MIDI + CLAP embedding → codec tokens | MIT code (weights licence not stated) | 2025 | n/a |
| DiffSinger (OpenVPI) | Score → mel + variance curves → vocoder | Apache-2.0 | Active community | Offline (ONNX) |
| SingingVocoders | NSF-HiFiGAN / UnivNet / DDSP-GAN training | MIT | n/a | — |
| BigVGAN-v2 / Vocos / HiFi-GAN / SiFi-GAN / NSF | Neural vocoders | MIT / MIT / MIT / MIT / BSD-3 | BigVGAN final checkpoints Sep 2024; Vocos 0.1.0, Oct 2023 | Vocos and HiFi-GAN faster than real time on CPU |
| DDSP-SVC / RVC (Applio) / so-vits-svc-fork / Seed-VC | Voice and singing conversion | MIT / MIT / MIT / **GPL-3.0** | DDSP-SVC 6.0 experimental; Applio maintained; so-vits-svc-fork "no longer maintained" | Yes (Seed-VC about 400 ms) |

#### A. DDSP family (interpretable, controllable, small)
- **magenta/ddsp:** a library of differentiable DSP blocks (synths, filters, reverb) used as output layers. It includes Colabs for timbre transfer (for example voice to violin) and autoencoder training. Requires TensorFlow ≥ 2.1. Paper at ICLR 2020. Apache-2.0 — [GitHub](https://github.com/magenta/ddsp). Last PyPI release 3.7.0, 25 May 2023 — [PyPI](https://pypi.org/project/ddsp/)
- **DDSP-VST, README:** "DDSP Effect" and "DDSP Synth" VST3/AU plug-ins built with JUCE; binaries for Windows and macOS. The build uses TFLite/XNNPACK. Apache-2.0 — [GitHub](https://github.com/magenta/ddsp-vst)
- **DDSP-VST, blog (8 Jun 2022):**
  - A real-time synth and effect.
  - Input is reduced to pitch, from a distilled "tiny CREPE" of about 160k parameters (roughly 137× smaller than the original), plus RMS loudness.
  - An RNN predicts harmonic and filtered-noise synth controls every 20 ms; this is 5× cheaper than every 4 ms.
  - Non-causal convolutions were avoided to keep latency down.
  - A MIDI-driven synth mode exists.
  - Users can train their own model from a few minutes of audio in a couple of hours on a free Colab GPU.
  — [Magenta blog](https://magenta.tensorflow.org/ddsp-vst-blog)
  - The repository was archived on 9 Oct 2024 and has no GitHub releases — [GitHub](https://github.com/magenta/ddsp-vst/releases)
- **MIDI-DDSP (ICLR 2022):**
  - A three-level hierarchy (notes → performance → synthesis) with controls for timbre, vibrato, dynamics and articulation — [arXiv](https://arxiv.org/abs/2112.09312)
  - Trained on URMP for 13 instruments: violin, viola, cello, double bass, flute, oboe, clarinet, saxophone, bassoon, trumpet, horn, trombone, tuba.
  - Six editable note-expression controls: volume, vol_fluc, vibrato, brightness, attack, vol_peak_pos. Synthesis parameters (f0, amplitudes, harmonic distribution, noise) are also editable.
  - Command-line synthesis "just like FluidSynth".
  - Built for Python 3.8 and TensorFlow 2.7.
  - Training took about 18 h on one RTX 8000, and >24 GB of GPU memory is recommended at batch size 16. Training on arbitrary datasets is not supported.
  - The Hugging Face Space is "no longer functional". Apache-2.0.
  — [GitHub](https://github.com/magenta/midi-ddsp)
  - Repository archived 1 Feb 2024 — [GitHub](https://github.com/magenta/midi-ddsp). Last PyPI release 0.2.6, 30 Nov 2022 — [PyPI](https://pypi.org/project/midi-ddsp/)
- **DDSP-Piano (IRCAM; DAFx 2022, JAES September 2023):**
  - Polyphonic piano synthesis from MIDI on top of TF DDSP 3.7.0.
  - Ten "piano years" learned from MAESTRO; 24 kHz by default; 250 Hz MIDI control rate.
  - Single-phase training is recommended. Apache-2.0.
  — [GitHub](https://github.com/lrenault/ddsp-piano)
- **acids-ircam ddsp_pytorch:** a PyTorch DDSP that exports to TorchScript. A Pure Data `ddsp~` external runs it in real time on the CPU, with pitch and loudness inlets. Pretrained saxophone and violin models at 48 kHz. Apache-2.0 — [GitHub](https://github.com/acids-ircam/ddsp_pytorch)
- **DDX7 (ISMIR 2022):** differentiable FM synthesis of instrument sounds, trained on URMP violin, flute and trumpet with torchcrepe pitch. Apache-2.0 — [GitHub](https://github.com/fcaspe/ddx7)
- **pc-ddsp (yxlllc):**
  - Two pitch-controllable DDSP vocoders: "Sins" (additive) and "CombSub" (comb-tooth subtractive). CombSub keeps the formants, and so the timbre, when the pitch is shifted.
  - Usable as a vocoder in OpenVPI DiffSinger.
  - The default config trains a 44.1 kHz vocoder on a GTX 1660.
  - Updates in 2023 and 2024, and again on 28 Sep 2026, tested with Python 3.11, CUDA 13.0 and torch 2.9.1 on Windows. MIT.
  — [GitHub](https://github.com/yxlllc/pc-ddsp)
- **SawSing / "DDSP-based Singing Vocoders" (ISMIR 2022):** the subtractive SawSinSub plus four other DDSP vocoders. Small models trained on one GPU with 3 h of data; a 3-minute-data experiment is also reported. Licence **AGPL-3.0** — [GitHub](https://github.com/YatingMusic/ddsp-singing-vocoders)

#### B. RAVE family (latent audio autoencoders, timbre transfer; non-commercial licence)
- **RAVE paper:** the first model to generate 48 kHz audio, "20 times faster than real-time on a standard laptop CPU", using two-stage training (representation learning, then adversarial fine-tuning) — [arXiv](https://arxiv.org/abs/2111.05011)
- **RAVE README:**
  - Minimum GPU memory by config: v1 8 GB; v2 16 GB; v2_small 8 GB; v3 32 GB; discrete 18 GB; onnx 6 GB; raspberry 5 GB.
  - A causal mode lowers latency. `--streaming` TorchScript export is needed for real-time use.
  - Style transfer through Adaptive Instance Normalization; pretrained streaming models are provided.
  - Licence **CC BY-NC 4.0**.
  — [GitHub](https://github.com/acids-ircam/RAVE)
  - Last PyPI release acids-rave 2.3.1, 18 Dec 2023 — [PyPI](https://pypi.org/project/acids-rave/)
- **nn~:** a Max/MSP and Pure Data external that wraps libtorch for RAVE and other TorchScript models. Since v1.6.0, models can be downloaded through the IRCAM Forum API. **CC BY-NC 4.0** — [GitHub](https://github.com/acids-ircam/nn_tilde). nn-tilde 1.6.0 on PyPI, 22 May 2025 — [PyPI](https://pypi.org/project/nn-tilde/)
- **rave_vst:** "This project has been archived… You should not expect any update". **CC BY-NC 4.0** — [GitHub](https://github.com/acids-ircam/rave_vst). A RAVE VST beta is distributed on the IRCAM Forum — [RAVE README](https://github.com/acids-ircam/RAVE)
- **BRAVE (JAES 2025):** a low-latency variant of RAVE for instrumental performance. The Minifusion plug-in runs BRAVE models at under 10 ms latency with about 3 ms jitter. Trained with the `rave` command-line tool. **CC BY-NC 4.0** — [GitHub](https://github.com/fcaspe/BRAVE). Reproduces pitch and loudness better than RAVE, with similar timbre modification — [arXiv](https://arxiv.org/abs/2503.11562)
- **RAVE on saxophone (SMC 2024):** a layer-by-layer analysis of pretrained RAVE models on tenor saxophone. Multiphonics were poorly distinguished. Quality was judged only by one saxophonist's listening — [SMC 2024](https://smcnetwork.org/smc2024/papers/SMC2024_paper_id91.pdf)

#### C. Deployment SDKs and real-time runtimes
- **Neutone SDK v1.5.2:**
  - Wraps PyTorch models (TorchScript) for the free hosts Neutone FX (real-time) and Neutone Gen (non-real-time, beta; one example model is Stable Audio Open Small).
  - Handles buffering, sample-rate and stereo/mono conversion, and delay compensation.
  - Includes a DDSP timbre-transfer example.
  - Licence LGPL-2.1. Paper at AES AIMLA 2025.
  — [GitHub](https://github.com/Neutone/neutone_sdk). PyPI release 13 Nov 2025 — [PyPI](https://pypi.org/project/neutone-sdk/)
- **anira:** real-time-safe neural network inference for audio apps, with LibTorch, ONNX Runtime, LiteRT/TFLite and ExecuTorch backends. Apache-2.0. Active, with a user survey running September–October 2026 — [GitHub](https://github.com/anira-project/anira)
- **RTNeural:** lightweight C++ inference (Dense, GRU, LSTM, Conv1D/2D and more) designed for real-time audio. BSD-3 — [GitHub](https://github.com/jatinchowdhury18/RTNeural)

#### D. Large generative and MIDI-conditioned models
- **music-spectrogram-diffusion (ISMIR 2022):**
  - MIDI goes to a spectrogram through an encoder-decoder Transformer (DDPM decoder), then to audio through a GAN spectrogram inverter. It handles arbitrary instrument combinations and trains on transcription datasets.
  - The DDPM decoder beat the autoregressive one.
  - On Colab TPUs, `base_with_context` renders about 5× slower than real time; the paper's speeds need a TPUv4.
  - Apache-2.0.
  — [GitHub](https://github.com/magenta/music-spectrogram-diffusion)
  - Repository archived 6 Jan 2026 — [GitHub](https://github.com/magenta/music-spectrogram-diffusion)
- **Magenta RealTime v1:** code Apache-2.0, weights CC-BY 4.0. Steered by text or audio prompts. Generates 2-second chunks with a 10-second context; runs on Colab TPUs; no MIDI — [Hugging Face](https://huggingface.co/google/magenta-realtime). Technical report August 2025 — [arXiv](https://arxiv.org/abs/2508.04651)
- **Magenta RealTime 2, announcement (4 Jun 2026):**
  - Two sizes: 230M ("small") and 2.4B ("base").
  - Controls: text and audio style prompts, MIDI note control, drums on/off.
  - Output 48 kHz stereo via the SpectroStream codec (25 Hz tokens, 40 ms frames); about 200 ms control latency.
  - Real time only on Apple Silicon (MLX). Fine-tuning is "upcoming".
  — [Magenta](https://magenta.withgoogle.com/magenta-realtime-2)
- **Magenta RealTime 2, model card:** MIDI input is a 128-dimensional multi-hot vector per frame, with Off/Sustain/Onset/"Sustain or onset" states. Trained on about 71k hours of mostly instrumental stock music. Code Apache-2.0, weights CC-BY 4.0 — [Hugging Face](https://huggingface.co/google/magenta-realtime-2)
- **Magenta RealTime 2, repository:** both sizes can run offline (not in real time) on any Apple Silicon Mac or an NVIDIA GPU through the Python library (JAX/MLX). A C++ engine targets Apple Silicon, and a "jam" example app explores note control — [GitHub](https://github.com/magenta/magenta-realtime). magenta-rt 2.0.3 on PyPI, 30 Jul 2026 — [PyPI](https://pypi.org/project/magenta-rt/)
- **Stable Audio Open 1.0:**
  - About 1B parameters; up to 47 s of 44.1 kHz stereo from text (T5 encoder) plus timing.
  - Trained on 486,492 CC0 / CC-BY / CC Sampling+ recordings from Freesound and the Free Music Archive.
  - Cannot produce realistic vocals, and is better at sound effects than music.
  - Licence: Stability AI Community License.
  — [Hugging Face](https://huggingface.co/stabilityai/stable-audio-open-1.0)
- **Stable Audio Open Small:** about 0.5B parameters per the model card; up to 11 s, 44.1 kHz stereo; text-only conditioning; Arm CPU optimisation; Community License; paper May 2025 — [Hugging Face](https://huggingface.co/stabilityai/stable-audio-open-small)
- **Stability AI Community License:** free commercial use for organisations under US$1M annual revenue; an Enterprise licence is required above that. Core Models and their outputs may not be used to create new foundational model architectures — [Stability AI](https://stability.ai/license)
- **stable-audio-tools:** MIT training and inference code — [GitHub](https://github.com/Stability-AI/stable-audio-tools). Latest PyPI release 0.0.20, 20 May 2026 — [PyPI](https://pypi.org/project/stable-audio-tools/)
- **ACE-Step v1 (May 2025):** generates 4 minutes of music in 20 s on an A100. "StemGen" (a ControlNet-LoRA) generates individual instrument stems; a "Text2Samples" LoRA generates instrument loops. Peak VRAM was cut to 8 GB on 10 May 2025. Apache-2.0 — [GitHub](https://github.com/ace-step/ACE-Step)
- **ACE-Step 1.5 (technical report February 2026; XL 4B released 2 Apr 2026):**
  - Runs locally with under 4 GB of VRAM. On ≤6 GB cards it uses the 2B turbo DiT only, with INT8 quantization and full CPU offload.
  - Features: cover, repaint, extract/lego/complete, track separation, multi-track "add layer", and BPM/key metadata control.
  - LoRA training: 8 songs in 1 hour on an RTX 3090 (12 GB VRAM).
  - Self-reported quality "between Suno v4.5 and Suno v5". A Windows portable package exists. MIT.
  - MIDI input is not among the listed controls.
  — [GitHub](https://github.com/ace-step/ACE-Step-1.5)

#### E. Score-to-audio and MIDI-to-audio research (2019–2026)
- **Zhao, Wang, Juvela, Yamagishi (2019; ICASSP 2020):** transferred speech vocoders (WaveNet, WaveGlow, NSF) to instrument sound generation. All three improved when pre-trained on speech and then fine-tuned on music. NSF was best except in zero-shot, with samples perceptually close to natural audio — [arXiv](https://arxiv.org/abs/1910.12381)
- **PerformanceNet (2019):** a CNN for score-to-audio generation — [ar5iv](https://ar5iv.arxiv.org/html/1905.11689) (title only seen)
- **Deep Performer (Dong et al., February 2022):**
  - A TTS-inspired Transformer encoder-decoder for score-to-audio, with new techniques for polyphonic input and fine-grained conditioning.
  - Introduces a new violin dataset of recordings, scores and alignments.
  - Competitive with the baseline on violin; significantly better on piano.
  — [arXiv](https://arxiv.org/abs/2202.06034)
- **Kim, Choi, Nam (January 2024; ICASSP 2024):** expressive polyphonic acoustic guitar synthesis using a guitar-specific "guitarroll" input and diffusion outpainting for long-term consistency. Extra training data came from a high-quality sample-based guitar synth. Better quality and more realistic timbre than the prior approach — [arXiv](https://arxiv.org/abs/2401.13498); [KAIST demo](https://mac.kaist.ac.kr/expressive_sound_synthesis/expressive_sound_synthesis.html)
- **CoSaRef (Take & Akama, October 2024, revised June 2025):** MIDI is first rendered by concatenative synthesis from one-shot samples, then refined by a diffusion model. No paired MIDI–audio data is needed. It beat a MIDI-supervised, timbre-controllable state-of-the-art method objectively and subjectively — [arXiv](https://arxiv.org/abs/2410.16785)
- **TokenSynth (February 2025):** a decoder-only Transformer generates neural-codec (DAC) tokens from MIDI tokens plus a CLAP timbre embedding. It supports zero-shot instrument cloning, text-to-instrument and text-guided timbre manipulation — [arXiv](https://arxiv.org/abs/2502.08939). Code is MIT, released as a pip package with pretrained weights on Hugging Face (weights licence not stated). The quickstart writes 16 kHz audio; it generates "polyphonic single-instrument" audio — [GitHub](https://github.com/KyungsuKim42/tokensynth)
- **MIDI-VALLE (ISMIR 2025):** a VALL-E-style neural-codec language model. It is conditioned on a reference recording and its MIDI, then renders target MIDI as piano audio. Fréchet Audio Distance is more than 75% lower than a state-of-the-art baseline on ATEPP and MAESTRO; the listening test favoured it 202 votes to 58 — [arXiv](https://arxiv.org/abs/2507.08530)
- **Latent Diffusion Bridges (Sony, September 2024; v4 January 2025):** unpaired timbre transfer with one diffusion model per instrument, trained on CocoChorales. Better FAD and pitch distance than VAEGAN and Gaussian Flow Bridges — [arXiv](https://arxiv.org/abs/2409.06096); repository listed at [GitHub](https://github.com/sony/diffusion-timbre-transfer)

#### F. Singing-voice stacks that could be adapted to instruments
- **OpenVPI DiffSinger:** Apache-2.0 — [GitHub](https://github.com/openvpi/DiffSinger). ONNX is the deployment format, with export of the variance model, the acoustic model and the NSF-HiFiGAN vocoder — [GettingStarted](https://github.com/openvpi/DiffSinger/blob/main/docs/GettingStarted.md)
- **DiffSinger variance curves:** besides pitch, variance models predict energy (deprecated), breathiness (RMS of the aperiodic part), voicing (RMS of the harmonic part) and tension (ratio of the fundamental to the full harmonics).
  - OpenUtau is the recommended production front-end.
  - Training uses 16-bit mixed precision by default; full FP32 (`32-true`) is available.
  - Fine-tuning and parameter freezing are supported.
  — [BestPractices](https://github.com/openvpi/DiffSinger/blob/main/docs/BestPractices.md)
- **OpenUtau:** the DiffSinger renderer has been merged into official OpenUtau. The "diffsingerpack" build ships with a vocoder — [GitHub](https://github.com/xunmengshe/OpenUtau)

#### G. Neural vocoders relevant to instruments
- **HiFi-GAN:** MIT (2020) — [GitHub](https://github.com/jik876/hifi-gan)
- **NSF family (NII):** BSD-3-Clause — [GitHub](https://github.com/nii-yamagishilab/project-NN-Pytorch-scripts). Best for instruments in the transfer study above — [arXiv](https://arxiv.org/abs/1910.12381)
- **BigVGAN-v2 (July 2024; final 5M-step checkpoints September 2024):**
  - Trained on diverse audio including speech, environmental sounds and instruments; up to 44 kHz and 512× upsampling.
  - 112–122M parameters (the v1 "base" models are 14M); optional fused CUDA kernel.
  - On an RTX 2080 Ti it runs 21.5–44.5× real time and uses 1.3–5.0 GB of VRAM depending on input length.
  - MIT.
  — [GitHub](https://github.com/NVIDIA/BigVGAN). PyPI bigvgan 2.4.1, 27 Oct 2024 — [PyPI](https://pypi.org/project/bigvgan/)
- **Vocos:**
  - Speed (13.5M parameters): 6,696.52× real time on GPU and 169.63× on CPU. HiFi-GAN reaches 495.54× / 5.84×, and BigVGAN (14M) 98.61× / 0.40×.
  - Although trained only on LibriTTS speech, on MUSDB18 music it scored ViSQOL 4.55, against 4.54 for BigVGAN and 4.39 for HiFi-GAN.
  — [Vocos paper](https://arxiv.org/pdf/2306.00814)
  - MIT; PyPI 0.1.0, 14 Oct 2023. The README says maintainers are still reviewing focused improvements — [GitHub](https://github.com/gemelo-ai/vocos); [PyPI](https://pypi.org/project/vocos/)
- **OpenVPI SingingVocoders:**
  - Configs for NSF-HiFiGAN, DDSP-GAN, NSF-UnivNet (recommended), an octave-ignoring "chroma" NSF-HiFiGAN, and LVC-DDSP.
  - The community NSF-HiFiGAN can be fine-tuned at 44.1 kHz in about 2,000 steps on small data. The default training config targets a 24 GB GPU.
  - Exported weights work in DDSP-SVC, Diffusion-SVC, so-vits-svc and DiffSinger. MIT.
  — [GitHub](https://github.com/openvpi/SingingVocoders)
  - DDSP-SVC uses the OpenVPI NSF-HiFiGAN 44.1 kHz / hop 512 / 128-bin checkpoint (2024.02) — [DDSP-SVC](https://github.com/yxlllc/DDSP-SVC)
- **SiFi-GAN:** a source-filter HiFi-GAN that is fast and pitch-controllable. MIT — [GitHub](https://github.com/chomeyama/SiFiGAN)

#### H. Voice and singing conversion, and audio-to-MIDI helpers
- **DDSP-SVC:**
  - MIT. Training and synthesis need much less hardware than so-vits-svc, and training speed is close to RVC.
  - Version history: 3.0 added shallow diffusion; 4.0 and 5.0 are cascade diffusion models with a real-time GUI; 6.0 is an experimental rectified-flow model (offline only).
  - Uses a ContentVec or HuBERT encoder, RMVPE pitch and an NSF-HiFiGAN vocoder.
  - The real-time front end uses SOLA cross-fading.
  - The README admits raw DDSP quality "is not ideal" without an enhancer or shallow diffusion.
  — [GitHub](https://github.com/yxlllc/DDSP-SVC)
- **so-vits-svc-fork:**
  - Real-time support; marked "No Longer Maintained".
  - Training needs at least 4 GB of VRAM. GPU inference needs at least 4 GB, or CPU inference "is fast enough".
  - Colab is recommended for anyone without a GPU over 10 GB. MIT.
  - The same README calls the original RVC "no longer maintained", Applio (MIT) "actively maintained", and VCClient "not quite actively maintained".
  — [GitHub](https://github.com/voicepaw/so-vits-svc-fork)
  - Yet PyPI shows release 4.2.30 on 2 Feb 2026 — [PyPI](https://pypi.org/project/so-vits-svc-fork/)
- **RVC:** MIT. The README gives Windows install paths for NVIDIA (CUDA 11.8 builds for cards before RTX 50; CUDA 12.8 for RTX 50) and DirectML for AMD/Intel, and uses RMVPE in ONNX form — [GitHub](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI). The RTX 50 instructions suggest recent edits, which conflicts with the "no longer maintained" label above.
- **Applio:** code and weights MIT; commercial use permitted — [GitHub](https://github.com/IAHispano/Applio)
- **Seed-VC:** zero-shot voice and singing conversion. Real-time mode has about 300 ms algorithm delay plus about 100 ms device delay (measured on an RTX 3060 Laptop). The singing model is 200M parameters at 44.1 kHz with a BigVGAN vocoder. Licence **GPL-3.0** — [GitHub](https://github.com/Plachtaa/seed-vc)
- **w-okada VCClient:** supports RVC and Beatrice v2, with CUDA and ONNX builds for Windows. MIT — [GitHub](https://github.com/w-okada/voice-changer)
- **Basic Pitch (Spotify):** Apache-2.0; ICASSP 2022. Polyphonic and instrument-agnostic; installs the ONNX model by default on Windows. Version 0.4.0, 16 Aug 2024 — [GitHub](https://github.com/spotify/basic-pitch); [PyPI](https://pypi.org/project/basic-pitch/)
- **NeuralNote v2.0.0:** Apache-2.0. Replaced Basic Pitch with a new transcription model. Windows builds are VST3 and Standalone — [GitHub](https://github.com/DamRsn/NeuralNote)

### Inferences
- **Code health.** Google's TensorFlow DDSP stack is effectively frozen (archived, last releases 2022–2023). New work should start from maintained PyTorch descendants (pc-ddsp, ddsp_pytorch, DDSP-SVC, the OpenVPI tools) or a small rewrite. DDSP's core (harmonic oscillator bank, filtered noise, reverb) is simple enough to port.
- **Licence traps:**
  - Avoid in anything that may become commercial: RAVE, nn~, rave_vst and BRAVE (CC BY-NC); SawSing (AGPL); Seed-VC (GPL).
  - Watch: Neutone SDK (LGPL, so dynamic-linking obligations); Stable Audio models (Community License, free under US$1M revenue).
  - Permissive: DDSP family, DiffSinger, ACE-Step (Apache); pc-ddsp, DDSP-SVC, RVC/Applio, HiFi-GAN, Vocos, BigVGAN, SingingVocoders, SiFi-GAN (MIT); NSF (BSD-3); Magenta RT (Apache code, CC-BY weights).
  - Pretrained weights can inherit dataset restrictions. For example, ddsp-piano weights trained on MAESTRO, which is CC BY-NC-SA.
- **Rough quality ladder.** Codec language models and diffusion (MIDI-VALLE, TokenSynth, spectrogram diffusion, CoSaRef) beat mel-spectrogram plus NSF/BigVGAN pipelines (DiffSinger-style), which beat raw DDSP. Compute and data needs rise in the same order. DDSP-SVC's fix (an enhancer or shallow diffusion on top of DDSP) is a middle path.
- **Real time on CPU** is realistic for DDSP and DDX7, RAVE and BRAVE (licence permitting), Vocos and HiFi-GAN. Diffusion and codec-LM renderers are not; Magenta RT 2 manages real time only on Apple Silicon.
- **Real time is optional for a VOCALOID-like workflow.** Yamaha's system and Dreamtonics' approach read the whole score before rendering, so offline rendering is acceptable for an MVP. Real time matters only for live playing or previews.

### Gaps
- Last-commit dates for many repositories (DiffSinger, SingingVocoders, DDSP-SVC, RVC, ddsp-piano, ddsp_pytorch, BRAVE, TokenSynth) could not be retrieved, because the GitHub API was blocked and fetched pages showed no dates. Activity above comes from README text and PyPI.
- Code or weights availability for Deep Performer, guitar diffusion outpainting, CoSaRef and MIDI-VALLE was not confirmed. TokenSynth's weights licence and training data are unknown.
- No maintained, published DiffSinger or RVC instrument models were found, and no MOS comparison of open instrument synthesizers on common data.
- Stable Audio Open Small's parameter count (about 0.5B on the model card) was not checked against the paper.

## 3. Datasets usable for training instrument models

### Takeaway
Permissive (CC BY) datasets exist for many instrument families: NSynth, Slakh, MusicNet, GuitarSet, TinySOL, CocoChorales and ChoraleBricks. But the best note-aligned, expressive solo recordings (URMP, Bach10) have no stated licence. The main piano set (MAESTRO) is non-commercial, and the large permissive sets are often synthetic (Slakh rendered from sample libraries, CocoChorales from MIDI-DDSP, NSynth one-shots). For a commercial-leaning MVP, use CC BY data for prototyping and plan your own recordings (DDSP-scale models need only minutes per instrument).

### Cited Findings
- **URMP:**
  - 44 pieces (11 duets, 12 trios, 14 quartets, 7 quintets); 12.5 GB download — [URMP](https://labsites.rochester.edu/air/projects/URMP.html)
  - 13 instruments: violin, viola, cello, double bass, flute, oboe, clarinet, saxophone, bassoon, trumpet, horn, trombone, tuba.
  - Separate tracks as 48 kHz / 24-bit mono WAV. Frame-level F0 (46 ms window, 10 ms hop) and note-level annotations. MIDI scores plus PDF sheet music, and 1080p video.
  - About 80 minutes in total (sum of Table 1).
  - No licence is stated: download is through a Google form, and users are asked to cite the paper.
  — [URMP documentation](https://labsites.rochester.edu/air/projects/URMP/URMP_doc.pdf)
  - Used to train MIDI-DDSP and DDX7 — [MIDI-DDSP](https://github.com/magenta/midi-ddsp); [DDX7](https://github.com/fcaspe/ddx7)
- **Bach10:** 10 four-part Bach chorales, each part recorded separately: violin (soprano), clarinet (alto), saxophone (tenor) and bassoon (bass). Includes MIDI scores, frame-level F0 and note ground truth, and audio-to-MIDI alignment. Freely downloadable after a usage-tracking form; no licence named — [Bach10 documentation](https://labsites.rochester.edu/air/datasets/Bach10%20Dataset_v1.0.pdf)
- **ChoraleBricks (TISMIR 2025):** 10 chorales with 4 parts each, recorded on flute, oboe, clarinet, trumpet, saxophone, baritone, trombone and tuba. Includes sheet music, time-aligned symbolic scores, and F0 and note-event annotations. Data is CC BY 4.0; the sheet music is excluded — [AudioLabs Erlangen](https://audiolabs-erlangen.com/resources/MIR/2025-ChoraleBricks)
- **NSynth:** 305,979 four-second notes from 1,006 instruments taken from commercial sample libraries. 16 kHz mono, MIDI pitches 21–108, 5 velocities, 11 families, acoustic/electronic/synthetic sources. CC BY 4.0 — [Magenta](https://magenta.tensorflow.org/datasets/nsynth)
- **MAESTRO v3.0.0:** 198.7 h and 1,276 performances, with MIDI aligned to about 3 ms. 44.1–48 kHz WAV recorded on Yamaha Disklaviers at the Piano-e-Competition. **CC BY-NC-SA 4.0** — [Magenta](https://magenta.tensorflow.org/datasets/maestro)
- **GuitarSet:** acoustic guitar recorded through a hexaphonic pickup, with pitch contours, string and fret positions, chords, beats and playing style. CC BY 4.0 on Zenodo — [Zenodo](https://zenodo.org/records/3371780). mirdata lists 360 tracks and an MIT licence, which conflicts with Zenodo — [mirdata](https://mirdata.readthedocs.io/en/stable/source/quick_reference.html)
- **Slakh2100:** 2,100 mixtures (about 145 h) rendered from Lakh MIDI with sample-based virtual instruments (34 classes, 187 patches). 44.1 kHz FLAC stems with aligned MIDI. CC BY 4.0 — [Slakh](http://www.slakh.com/). mirdata lists 1,710 tracks — [mirdata](https://mirdata.readthedocs.io/en/stable/source/quick_reference.html)
- **MusicNet:** 330 freely licensed classical recordings with over 1 million note labels (instrument, onset, metrical position) and an estimated 4% label error. CC BY 4.0 — [Zenodo](https://zenodo.org/records/5120004)
- **CocoChorales:**
  - 240,000 examples (60,000 mixes for each of 4 ensemble types), over 1,400 h, 16 kHz.
  - Generated by Coconet (composition) and MIDI-DDSP (synthesis, trained on URMP).
  - Includes note-expression labels and 250 Hz synthesis parameters.
  - About 2.9 TB compressed. CC BY 4.0.
  — [Magenta](https://magenta.tensorflow.org/datasets/cocochorales)
- **Other datasets** (track counts and licences per [mirdata](https://mirdata.readthedocs.io/en/stable/source/quick_reference.html)):

  | Dataset | Tracks | Licence |
  |---|---|---|
  | Groove MIDI | 1,150 | CC BY-SA 4.0 |
  | TinySOL | 2,913 | CC BY 4.0 |
  | Good-Sounds | 16,308 | CC BY-SA 4.0 |
  | Dagstuhl ChoirSet | 108 | CC BY 4.0 |
  | Medley-solos-DB | 21,571 | CC BY-SA 4.0 |
  | MedleyDB melody/pitch | — | CC BY-NC-SA 4.0 (audio on request) |
  | PHENICX-Anechoic | 4 | CC BY-NC-SA 4.0 |
  | IRMAS | 9,579 | CC BY-NC-SA 3.0 |
  | IDMT-SMT-Audio-Effects | — | CC BY-NC-ND 4.0 |
  | Filosax (saxophone) | 48 | Licence not available |

- **Training data of the large models:** Magenta RT 2 used about 71k hours of stock music — [Hugging Face](https://huggingface.co/google/magenta-realtime-2). Stable Audio Open used only CC0, CC-BY and CC Sampling+ Freesound/FMA recordings — [Hugging Face](https://huggingface.co/stabilityai/stable-audio-open-1.0)

### Inferences
- **URMP size.** About 80 minutes across 13 instruments means only minutes per instrument, often in ensemble context. That suits DDSP-scale models (DDSP-VST trains on a few minutes) but is thin for mel or diffusion models.
- **Commercial-safe candidates:** NSynth, Slakh, MusicNet, GuitarSet (per Zenodo), TinySOL, CocoChorales, ChoraleBricks, Dagstuhl ChoirSet (CC BY); Groove MIDI and Good-Sounds (CC BY-SA, share-alike). Caveat: Slakh and CocoChorales are synthetic, so a model would learn the sound of sample libraries or of MIDI-DDSP.
- **Non-commercial:** MAESTRO, MedleyDB, IRMAS, PHENICX, IDMT-SMT. **Licence unclear** (treat as research-only until clarified): URMP, Bach10, Filosax.
- **Own recordings are the cleanest route for commercial use and for expressive coverage.** A few minutes to an hour per instrument of legato, vibrato, dynamics sweeps and attacks, recorded dry and monophonic, fits DDSP and pc-ddsp training and avoids licence ambiguity.

### Gaps
- URMP and Bach10 licence terms are not stated anywhere found.
- MusicNet's total hours and GuitarSet's hours and player count are not on the pages fetched.
- No large, CC BY, note-aligned, expressive solo string or wind dataset was found beyond ChoraleBricks and URMP.

## 4. What can run or train locally on a Windows 11 laptop (GTX 1650 4 GB, Ryzen 7 5800H, 16 GB RAM) versus what needs Colab or cloud

### Takeaway
**Inference that fits the laptop:** small models such as DDSP and pc-ddsp, the Vocos, HiFi-GAN and NSF vocoders, DiffSinger exported to ONNX, RVC-class conversion, and even ACE-Step 1.5 in its INT8 / CPU-offload mode.

**Training that fits:** tiny DDSP-style models and vocoder fine-tunes, in FP32 with small batches.

**Training that needs Colab or cloud:**
- RAVE (5–32 GB depending on config);
- MIDI-DDSP (>24 GB recommended);
- BigVGAN-v2 (8×A100);
- ACE-Step LoRAs (12 GB);
- codec-LM and diffusion score-to-audio models.

**Three Windows/GPU traps:**
1. GTX 16-series cards are unstable in FP16, so train in FP32.
2. TensorFlow supports the GPU on native Windows only up to version 2.10 (affects DDSP, MIDI-DDSP and ddsp-piano).
3. JAX has no native Windows NVIDIA GPU support, only experimental WSL2 (affects Magenta RT and spectrogram diffusion).

### Cited Findings
- **GTX 1650 Laptop:** Turing TU117, 1,024 shaders (896 on some variants), no Tensor or RT cores, up to 4 GB GDDR5/GDDR6 on a 128-bit bus (192 GB/s), 50 W TGP (the Max-Q variant is 15 W lower) — [Notebookcheck](https://www.notebookcheck.net/NVIDIA-GeForce-GTX-1650-Laptop-Graphics-Card.416044.0.html)
- **FP16 on GTX 16-series:** GTX 1650/1660/1660 Ti/1660 Super produce all-black or all-green images in half precision in ComfyUI, which the article calls a known fp16 defect. The fix is forcing FP32, which is slower — [RunAIHome blog, 2026](https://www.runaihome.com/blog/comfyui-black-image-output-fix-2026/) (community source; image models, not audio)
- **DiffSinger precision:** trains in 16-bit mixed precision by default; set `pl_trainer_precision: 32-true` to use FP32 — [DiffSinger BestPractices](https://github.com/openvpi/DiffSinger/blob/main/docs/BestPractices.md)
- **TensorFlow on Windows:** "TensorFlow 2.10 was the last TensorFlow release that supported GPU on native-Windows"; 2.11 and later need WSL2 or the DirectML plugin — [TensorFlow](https://www.tensorflow.org/install/pip). DDSP needs TF ≥ 2.1 — [GitHub](https://github.com/magenta/ddsp). MIDI-DDSP was developed on TF 2.7 / Python 3.8 — [GitHub](https://github.com/magenta/midi-ddsp)
- **JAX on Windows:** native Windows: CPU yes, NVIDIA GPU no. WSL2: NVIDIA GPU "experimental" — [JAX docs](https://docs.jax.dev/en/latest/installation.html). Magenta RT's Python library uses JAX or MLX — [GitHub](https://github.com/magenta/magenta-realtime)
- **ONNX Runtime and Windows ML:** the DirectML execution provider needs a DirectX 12 GPU (NVIDIA Kepler / GTX 600 and newer). "DirectML is in sustained engineering", with new work going to Windows ML — [ONNX Runtime docs](https://onnxruntime.ai/docs/execution-providers/DirectML-ExecutionProvider.html). Windows ML became generally available on 23 Sep 2025; it requires Windows 11 24H2+, and its NVIDIA execution provider is TensorRT for RTX (RTX GPUs) — [Windows Developer Blog](https://blogs.windows.com/windowsdeveloper/2025/09/23/windows-ml-is-generally-available)
- **Free Colab:** "notebooks can run for at most 12 hours"; GPU access "heavily restricted" and not guaranteed — [Colab FAQ](https://research.google.com/colaboratory/faq.html)
- **Stated compute needs, by project:**
  - RAVE minimum GPU memory: 5 GB (raspberry config), 6 GB (onnx), 8 GB (v1, v2_small), 16 GB (v2), 18 GB (discrete), 32 GB (v3) — [RAVE](https://github.com/acids-ircam/RAVE)
  - MIDI-DDSP: about 18 h on an RTX 8000; >24 GB recommended at batch size 16 — [MIDI-DDSP](https://github.com/magenta/midi-ddsp)
  - DDSP-VST trainer: a few minutes of audio, a couple of hours on a free Colab GPU — [Magenta blog](https://magenta.tensorflow.org/ddsp-vst-blog)
  - pc-ddsp: the default 44.1 kHz config is sized for a GTX 1660 — [pc-ddsp](https://github.com/yxlllc/pc-ddsp)
  - SawSing: one RTX 3090 Ti and 3 h of data — [GitHub](https://github.com/YatingMusic/ddsp-singing-vocoders)
  - so-vits-svc-fork: training ≥4 GB VRAM; GPU inference ≥4 GB, or CPU; Colab if the GPU has <10 GB — [GitHub](https://github.com/voicepaw/so-vits-svc-fork)
  - SingingVocoders: default config for a 24 GB GPU; fine-tunes in about 2,000 steps — [GitHub](https://github.com/openvpi/SingingVocoders)
  - BigVGAN-v2: trained on 8×A100; inference uses 1.3–1.7 GB VRAM for 256–2,048 mel frames, and 3.2–5.0 GB for 16,384 frames — [GitHub](https://github.com/NVIDIA/BigVGAN)
  - ACE-Step 1.5: "less than 4GB of VRAM" (≤6 GB means 2B turbo DiT only, INT8, full CPU offload); LoRA training needs 12 GB — [GitHub](https://github.com/ace-step/ACE-Step-1.5). ACE-Step v1 peaks at 8 GB — [GitHub](https://github.com/ace-step/ACE-Step)
  - Magenta RT 2: 230M or 2.4B parameters; real time on Apple Silicon only; offline on NVIDIA via Python — [GitHub](https://github.com/magenta/magenta-realtime)
  - music-spectrogram-diffusion: about 5× slower than real time on a Colab TPU — [GitHub](https://github.com/magenta/music-spectrogram-diffusion)
- **CPU speed references:**
  - Vocos 169.63×, HiFi-GAN 5.84× and BigVGAN (14M) 0.40× real time on CPU — [Vocos paper](https://arxiv.org/pdf/2306.00814)
  - RAVE: 20× real time on a laptop CPU — [arXiv](https://arxiv.org/abs/2111.05011)
  - DDSP-VST: a real-time plug-in with 20 ms control frames — [Magenta blog](https://magenta.tensorflow.org/ddsp-vst-blog)
  - The ddsp_pytorch Pd external runs on CPU — [GitHub](https://github.com/acids-ircam/ddsp_pytorch)
  - SWAM: about 52 MB RAM per instance; Core 2 Duo-class minimum CPU — [Audio Modeling](https://audiomodeling.com/strings/swam-viola)
  - Instrument X: no dedicated GPU required — [Dreamtonics](https://dreamtonics.com/?p=4621)
- **Deployment formats:**
  - DiffSinger deploys as ONNX — [GettingStarted](https://github.com/openvpi/DiffSinger/blob/main/docs/GettingStarted.md)
  - RAVE has an "onnx" config and streaming TorchScript export — [RAVE](https://github.com/acids-ircam/RAVE)
  - DDSP-VST is built on TFLite/XNNPACK — [GitHub](https://github.com/magenta/ddsp-vst)
  - Neutone uses TorchScript `.nm` files — [GitHub](https://github.com/Neutone/neutone_sdk)
  - anira supports LibTorch, ONNX Runtime, LiteRT and ExecuTorch — [GitHub](https://github.com/anira-project/anira)
  - Basic Pitch ships ONNX on Windows — [GitHub](https://github.com/spotify/basic-pitch)
  - VCClient has ONNX builds for RVC and Beatrice on Windows — [GitHub](https://github.com/w-okada/voice-changer)
  - RVC has Windows CUDA and DirectML install paths — [GitHub](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)
  - ACE-Step 1.5 offers a Windows portable package — [GitHub](https://github.com/ace-step/ACE-Step-1.5)

### Inferences
Feasibility on this laptop, based on the cited requirements (not measured on this hardware):

| Workload | GTX 1650 4 GB / CPU locally | Colab or cloud |
|---|---|---|
| DDSP / pc-ddsp / DDX7 per-instrument training (minutes to hours of audio) | **Yes**, FP32 with small batches and crops (pc-ddsp is sized for a 6 GB GTX 1660) | Optional, for faster iteration |
| DDSP inference, offline and real-time | **Yes, on CPU** | — |
| Vocos / HiFi-GAN / NSF inference | **Yes, on CPU**; BigVGAN-v2 on the GPU (1.3–1.7 GB VRAM for short chunks) | — |
| Fine-tuning NSF-HiFiGAN or pc-ddsp vocoders | Borderline: shrink the 24 GB default config, FP32 | Recommended (Colab GPU, when one is available) |
| DiffSinger acoustic/variance training | Borderline and unverified: FP32, small batches | Recommended |
| DiffSinger inference via ONNX | **Yes** (CPU, CUDA or DirectML; the OpenUtau precedent) | — |
| RVC / so-vits / DDSP-SVC training | Borderline (so-vits needs ≥4 GB) | Recommended |
| RVC / DDSP-SVC inference, including real time | **Yes** (GPU, or CPU for so-vits) | — |
| RAVE / BRAVE training | **No** (5–32 GB minimum) | Required (and CC BY-NC) |
| MIDI-DDSP training | **No** (>24 GB recommended; TF GPU on Windows ≤ 2.10) | Required |
| MIDI-DDSP / ddsp-piano inference | CPU feasible but slow; TF GPU needs TF ≤ 2.10 or WSL2 | Optional |
| ACE-Step 1.5 inference | Possible: 2B turbo DiT, INT8, CPU offload, LM disabled (16 GB system RAM may limit) | Better on ≥8–12 GB |
| ACE-Step LoRA training | **No** (12 GB) | Required |
| Magenta RT 2 | Real time: no (Apple Silicon only). Offline: small model only, on CPU or WSL2 GPU (experimental); base 2.4B too big for 4 GB | Linux GPU |
| Stable Audio Open Small inference | Probably yes on CPU (Arm-optimised; x86 speed unknown) | — |
| Codec-LM or diffusion score-to-audio training (TokenSynth, MIDI-VALLE, spectrogram diffusion) | **No** | Required |

- **Use PyTorch stacks on Windows.** They install CUDA builds natively (see RVC's and ACE-Step's Windows instructions). Avoid TensorFlow GPU (or pin TF 2.10, or use WSL2), and use JAX only through WSL2 or on Colab.
- **For deployment, export to ONNX and run with ONNX Runtime** (CPU execution provider by default; CUDA or DirectML providers as accelerators). Windows ML's NVIDIA path targets RTX cards, so a GTX 1650 would likely fall back to DirectML, CUDA or CPU.
- **Expect FP16/AMP problems on this GPU.** Train in FP32 with gradient accumulation instead of large batches, which DiffSinger supports.

### Gaps
- No measured benchmarks of these models on a GTX 1650 (Laptop) or a Ryzen 7 5800H were found. Real-time factors on this specific hardware are extrapolations.
- Whether the GTX 16-series FP16 problem also hits audio models (the source is about image diffusion) was not verified.
- Minimum VRAM for DiffSinger and RVC/Applio training is not stated in the sources read.
- How much system RAM ACE-Step 1.5 needs in CPU-offload mode was not found.

## 5. Most promising approaches for a solo developer's MVP (expressive instrument parts from MIDI, sharing infrastructure with a singing engine)

### Takeaway
The most realistic MVP is a VOCALOID-style two-stage renderer:

1. **Score/MIDI to expression curves.** Frame-level f0 with vibrato, glides and legato; loudness or "voicing"; noise or "breathiness"; brightness or "tension"; plus articulation tags.
2. **Curves to audio.** A small DDSP-type harmonic-plus-noise synthesizer (pc-ddsp CombSub/Sins or a ddsp_pytorch-style decoder), trained per instrument. An NSF or Vocos-type vocoder, or a light diffusion refiner, can be added for realism.

Start with monophonic strings, winds and brass. This design is what MIDI-DDSP, Yamaha's AI wind synthesis and Instrument X's dynamics lane all point to. It reuses the singing engine's control curves (DiffSinger's pitch, voicing, breathiness and tension), runs on CPU, trains locally or on free Colab, and uses MIT/Apache code.

Use sample/SFZ or physical-model rendering for polyphonic instruments (piano, guitar) in v1. Treat neural refinement (CoSaRef-style render-then-refine, TokenSynth, Magenta RT 2) and voice-to-instrument conversion (RVC/DDSP-SVC) as phase-2 features.

### Cited Findings
- **MIDI-DDSP** shows a note → performance → synthesis hierarchy with editable note-level expression controls: volume, volume fluctuation, vibrato, brightness, attack, peak position — [GitHub](https://github.com/magenta/midi-ddsp); [arXiv](https://arxiv.org/abs/2112.09312)
- **Yamaha's AI instrument synthesis** reads the whole score, infers vibrato and crescendo, and generates sound frame by frame from note sequences plus a dynamics parameter — [Yamaha](https://www.yamaha.com/en/tech-design/research/technologies/aisynth/)
- **Instrument X's controls** are an articulation editor, a single dynamics lane that changes timbre, phrase retakes and style presets — [Dreamtonics](https://dreamtonics.com/?p=4621)
- **DiffSinger's variance curves** (pitch, energy, breathiness, voicing, tension) are predicted from the score and drive the acoustic model; the stack deploys via ONNX in OpenUtau — [DiffSinger BestPractices](https://github.com/openvpi/DiffSinger/blob/main/docs/BestPractices.md); [GettingStarted](https://github.com/openvpi/DiffSinger/blob/main/docs/GettingStarted.md)
- **DDSP-VST** shows that per-instrument DDSP models can be trained from a few minutes of audio and run as real-time plug-ins — [Magenta blog](https://magenta.tensorflow.org/ddsp-vst-blog)
- **Raw DDSP quality** "is not ideal" for singing, but with an enhancer or shallow diffusion it can match so-vits-svc and RVC on some datasets — [DDSP-SVC](https://github.com/yxlllc/DDSP-SVC)
- **NSF-type vocoders** pre-trained on speech and fine-tuned on music give near-natural instrument audio — [arXiv](https://arxiv.org/abs/1910.12381)
- **pc-ddsp's CombSub** keeps timbre under pitch shift and plugs into DiffSinger as a vocoder; it was updated in September 2026 — [pc-ddsp](https://github.com/yxlllc/pc-ddsp)
- **Render-then-refine (CoSaRef)** reaches realism without paired MIDI–audio data — [arXiv](https://arxiv.org/abs/2410.16785)
- **TokenSynth** does zero-shot instrument cloning from MIDI plus a timbre embedding (MIT code) — [GitHub](https://github.com/KyungsuKim42/tokensynth)
- **Polyphonic neural synthesis is still at research grade:** guitar diffusion outpainting — [arXiv](https://arxiv.org/abs/2401.13498); MIDI-VALLE piano — [arXiv](https://arxiv.org/abs/2507.08530); DDSP-Piano — [GitHub](https://github.com/lrenault/ddsp-piano)
- **Sample playback building blocks:** sfizz (SFZ player) is BSD-2-Clause — [GitHub](https://github.com/sfztools/sfizz); FluidSynth is LGPL-2.1 — [GitHub](https://github.com/FluidSynth/fluidsynth)
- **Commercial voice-to-instrument precedent** (Kits.ai, SoundID VoiceAI, Neutone Morpho) and the ACE Studio reviewer's "scratch-sing → Vocal-to-MIDI → AI instrument" workflow — [Kits.ai](https://kits.ai/blog/ai-instruments-on-kits); [Sonarworks](https://www.sonarworks.com/blog/learn/can-you-turn-your-voice-into-an-instrument); [Sound On Sound](https://soundonsound.com/reviews/ace-studio-2)

### Inferences

#### Ranked options for the MVP
**A. Hierarchical DDSP renderer for monophonic instruments (recommended core).**
- **How it works:**
  - MIDI is turned into expression curves by rules first (vibrato after onset, crescendo envelopes, portamento on legato, CC1/CC11 mapped to dynamics), later by a small learned "expression model" in the spirit of MIDI-DDSP.
  - A per-instrument DDSP decoder trained on minutes to hours of solo audio turns the curves into audio.
  - Add a convolution-reverb or room stage.
- **Pros:**
  - Tiny models; CPU real-time and offline rendering.
  - Trainable on the GTX 1650 in FP32, or on free Colab.
  - Exact MIDI adherence, with interpretable, editable curves (piano-roll lanes like Instrument X's dynamics lane).
  - MIT/Apache code; ONNX-exportable.
  - Shares f0, loudness and noise curves with the singing engine.
- **Cons:**
  - Monophonic only.
  - Limited realism of attacks, transients and bow/breath noise without a refiner.
  - The TensorFlow reference code is archived, so it must be built on the PyTorch ports.
  - Articulation transitions (legato, staccato) need explicit modelling and data.

**B. Reuse the singing stack directly: DiffSinger-style acoustic and variance models plus an NSF-HiFiGAN or pc-ddsp vocoder, with articulation tokens in place of phonemes.**
- **Pros:**
  - Maximum code sharing with the voice engine (same editor, curves, ONNX runtime and OpenUtau-like integration).
  - Variance curves already exist; Apache/MIT licences.
  - NSF vocoders transfer well to instruments.
- **Cons:**
  - Needs note-aligned, articulation-labelled instrument data (URMP is small and has an unclear licence).
  - Heavier training: borderline on 4 GB, with FP16 issues.
  - No community instrument models found to start from.
  - Polyphony remains awkward.

**C. Sample-based or physical-model rendering for polyphonic and percussive instruments (piano, guitar, drums) in v1.**
- **Pros:** proven quality, zero training, permissive players (sfizz BSD-2), CPU-cheap.
- **Cons:** not "AI"; realism and licence depend on the sample sets; expression is limited to what the library offers.
- **Later:** DDSP-Piano-like models (MAESTRO weights are non-commercial) or research polyphonic models.

**D. Optional audio-to-audio stage: RVC/Applio or DDSP-SVC trained on solo instrument recordings.** This converts the singing engine's output, or a user's hum, into an instrument, as Kits.ai, SoundID VoiceAI and Morpho do.
- **Pros:** reuses the vocal pipeline; MIT; real-time capable; Applio is maintained.
- **Cons:**
  - Quality is bounded by the guide performance.
  - Content encoders (HuBERT/ContentVec) and the RMVPE pitch tracker were built for voice; how well they work on instruments is unverified.
  - Avoid RAVE/BRAVE for anything commercial (CC BY-NC) despite their excellent latency.

**E. Watch list / phase 2:**
- CoSaRef-style render-then-refine: concatenative or DDSP render, then a diffusion refiner. This could add realism on top of A or C.
- TokenSynth: MIT code, 16 kHz output, codec LM.
- Magenta RT 2 MIDI control: Apache code with CC-BY weights, but real time only on Apple Silicon and JAX-bound on Windows.
- ACE-Step 1.5: MIT; cover/repaint could restyle a rendered stem, but it has no MIDI input.
- None of these is a precise, lightweight MIDI renderer for a 4 GB Windows laptop today.

#### Suggested sequencing
1. MIDI to curves: rule-based expression, plus a curve editor shared with the singing engine.
2. One DDSP instrument (violin or flute), trained on own recordings or URMP for prototyping, rendered offline on CPU.
3. Add an NSF/Vocos-class or pc-ddsp vocoder and a small refiner if needed.
4. Add articulation and legato handling.
5. Add sample/SFZ fallback for polyphonic parts.
6. Optional voice-to-instrument (RVC/DDSP-SVC).
7. Later, experiment with diffusion or codec-LM refinement on Colab.

#### Main risks
- **Data licensing:** URMP/Bach10 are unclear and MAESTRO is non-commercial, so own recordings are the safe route.
- **Realism gap** versus Instrument X and SWAM for attacks and transitions.
- **Windows tooling:** TensorFlow/JAX GPU limits and FP16 on GTX 16-series.
- **Maintenance:** the reference implementations (DDSP-VST, MIDI-DDSP) are archived.

### Gaps
- No head-to-head listening test was found comparing DDSP, DiffSinger-style and codec-LM renderers trained on the same instrument data. The quality ranking above is inferred from separate papers and READMEs.
- How much data per instrument "Instrument X-level" realism needs is unknown; Dreamtonics has not disclosed architecture or data.
- No published evaluation of RVC/DDSP-SVC-style converters on instrument targets was found; the SMC 2024 study covers RAVE only.
