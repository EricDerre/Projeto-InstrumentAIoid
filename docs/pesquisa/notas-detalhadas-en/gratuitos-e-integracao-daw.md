# Free and open-source singing-voice synthesis on Windows (state on 8 October 2026): what is really free, free voicebanks, DAW integration (Cubase LE/AI 15, FL Studio 2024, REAPER) and Brazilian Portuguese

Reading guide: these notes complement, and try not to repeat, `../Apps de vocaloid e integrações/apps_comerciais_e_vozes_famosas.md` (commercial prices, VOCALOID6 trial/Lite, Synthesizer V and VoiSona pricing, famous-voice catalogue) and `../Apps de vocaloid e integrações/omnivocal_cubase15.md` (everything about Omnivocal). Facts reused from those notes are marked "(earlier notes)" and keep their original source links. OpenUtau wiki pages were read from copies saved on 6 Oct 2026 and are cited by their live GitHub URLs; release lists were re-read live on 8 Oct 2026. GitHub release pages show only day and month, so years marked "[year inferred]" come from release order. Target machine: Windows 11, Ryzen 7 5800H, 16 GB RAM, GTX 1650 4 GB, Cubase 15.0.30 (LE/AI-level licence, Omnivocal Beta 1.2.5 installed), FL Studio 2024 (24.2), REAPER 7.61.

## 1. Which free or open-source editors exist and are actively maintained in 2026 (version, date, download page, Windows requirements, GPU)?

### Takeaway
OpenUtau is the active hub of the free ecosystem: its "stable" build is still 0.1.565 (14 Sep 2025), but beta/alpha builds ship almost daily (0.1.573 Beta on 8 Oct 2026), and it hosts UTAU, DiffSinger, ENUNU/NNSVS and VOICEVOX voices. NEUTRINO (Tau v3.2.x, Apr–Sep 2026) and VOICEVOX (0.25.2, 30 Apr 2026) are the other maintained free engines. Classic UTAU is frozen at v0.4.19 (May 2024), TuneLab (v2.1.1, Sep 2026) is young and extension-based, and DiffScope still has no synthesis engine. The GPU is optional everywhere: it only speeds up neural engines (DirectML in OpenUtau/VOICEVOX, CUDA in NEUTRINO).

### Cited Findings

#### OpenUtau (open source, MIT): the active hub
- Download page is GitHub Releases. The release flagged "Latest" (stable) is still **0.1.565**, released "14 Sep", and the page notes "444 commits to master since this release" — [GitHub: OpenUtau latest release](https://github.com/stakira/OpenUtau/releases/latest); the wiki says "The latest stable version is 0.1.565 (09-14-2025)" — [OpenUtau wiki: Release Notes](https://github.com/stakira/OpenUtau/wiki/Release-Notes)
- Pre-releases visible on 8 Oct 2026 (all marked Pre-release):
  - 0.1.573 Beta (8 Oct): fixes native DirectML crashes on Windows (with CPU fallback), changes hifisampler loudness, offers to install a missing engine package and re-render, smoother UI.
  - 0.1.572.1–0.1.572.4 Alpha (3–7 Oct).
  - 0.1.571 Beta (3 Oct): "a DAW integration API connected to the UI, with an in-app bridge guide that detects the install" and "can install with one click", plus expression graphs, built-in hifisampler, Worldline-R1.1 and a Track Effects UI.
  - 0.1.570.13–.16 Alpha (29 Sep–2 Oct).
  — [GitHub: OpenUtau releases](https://github.com/stakira/OpenUtau/releases)
- Earlier betas:
  - 0.1.566 (28 Nov 2025): Worldline-R2 test renderer, microtonal tuning, merging vocal parts.
  - 0.1.567 (29 Nov 2025): Worldline-R2 removed "for now".
  - 0.1.568 (16 Mar 2026): new .ustx format 0.9 that "cannot be opened with previous versions of OpenUtau"; split part at playhead, theme editor, curve tools, attachable piano roll, trim/fade for wave parts, smooth pitch shape, audio-to-note transcription with GAME/RMVPE, and a "simple package manager".
  — [OpenUtau wiki: Release Notes](https://github.com/stakira/OpenUtau/wiki/Release-Notes)
- Windows prerequisites: the ".NET 8.0 Runtime" ("version 0.1.569 and later require the .NET 10 Runtime"); install the Visual C++ Redistributable if a "worldline" DLL error appears — [OpenUtau wiki: FAQ](https://github.com/stakira/OpenUtau/wiki/FAQ)
- It includes a default resampler and two wavtools that "should work on any platform", plus the WORLDLINE-R renderer; external UTAU resamplers work through the "Classic" renderer — [OpenUtau wiki: FAQ](https://github.com/stakira/OpenUtau/wiki/FAQ)
- "OpenUtau does not offer a default voicebank or mascot" — [OpenUtau wiki: FAQ](https://github.com/stakira/OpenUtau/wiki/FAQ)
- DiffSinger ("a machine learning based singing synthesizer"): first import the nsf_hifigan vocoder package. The wiki also says to turn on "beta" updates, because "some new voicebanks might use features not yet supported by the current stable build". Rendering speed-up is 50× by default — [OpenUtau wiki: DiffSinger support](https://github.com/stakira/OpenUtau/wiki/DiffSinger-support)
- GPU: "OpenUtau uses CPU to render by default. If you use Windows and have a discrete graphics card, you can use DirectML to make rendering faster". To enable it, set Machine Learning Runner to DirectML, choose the GPU and restart — [OpenUtau wiki: DiffSinger support](https://github.com/stakira/OpenUtau/wiki/DiffSinger-support)
- ENUNU/NNSVS support is "experimental". A separate ENUNU server (official ENUNU 0.4.0 for OpenUtau, or the unofficial ENUNUServer/SimpleEnunuServer) must be started before OpenUtau. Editing notes or lyrics is "very slow" because python.exe is started for every phrase — [OpenUtau wiki: ENUNU NNSVS Support](https://github.com/stakira/OpenUtau/wiki/ENUNU-NNSVS-Support)
- VOICEVOX: "OpenUtau supports VOICEVOX (humming function)". Install the full VOICEVOX editor, drag `VOICEVOX_Singer.zip` (from rokujyushi's fork) into OpenUtau, and keep VOICEVOX running. Phonemizers: S-VOICEVOX JA, S-VOICEVOX EN to JA, VOICEVOX JA — [OpenUtau wiki: VOICEVOX support](https://github.com/stakira/OpenUtau/wiki/VOICEVOX-support)
- Licence: MIT ("Copyright (c) 2014 StAkira") — [OpenUtau repository](https://github.com/stakira/OpenUtau)

#### Classic UTAU (freeware, Windows only): frozen
- The latest version is v0.4.19, dated 23 May 2024 and described as "セキュリティー脆弱性に対する更新です" (an update for a security vulnerability). A corrected installer, v0.4.19(c), followed on 24 May 2024 for a Windows 11 installer error. All older versions were withdrawn, and the zip version needs a separate VB6 runtime — [UTAU official site](http://utau2008.xrea.jp/)
- The page carries no licence or commercial-use text for the editor — [UTAU official site](http://utau2008.xrea.jp/)

#### NEUTRINO (free, closed source, Japanese singing)
- Downloads (read 8 Oct 2026):
  - Windows "Tau v3.2.2" (15 Apr 2026, 3.05 GB).
  - Windows bundled with the tuning-support tool, "Tau v3.2.4.ex" (2 Sep 2026, 1.53 GB).
  - macOS Tau v3.2.2.
  - Online (Google Colab) Tau v3.2.5 (25 Sep 2026).
  - Only the latest/final build of each generation is published; the EULA is dated 21 Aug 2026.
  — [NEUTRINO downloads](https://studio-neutrino.com/downloads/)
- "2026年9月現在、17名のキャラクターが公開されています" (17 characters published as of Sep 2026); the Tau v3.2.5 update was announced on 25 Sep 2026 — [NEUTRINO home](https://studio-neutrino.com/)
- Hardware:
  - From NEUTRINO -Muon v2.0, AVX2 is no longer required.
  - Recommended: a CPU with "Passmark score 10000以上", or a GPU, or the online version.
  - "GDDRメモリが4~6GB程度あれば問題無く動作" (about 4–6 GB of GPU memory runs without problems); CUDA core count and clock matter more than VRAM.
  - Old GPUs (e.g., GT730) are not supported by the NVIDIA toolkit. Use CPU mode instead by removing "-m" from Run.bat.
  - For out-of-GPU-memory errors: shorten phrases with rests or breath marks, or switch NSF to CPU.
  — [NEUTRINO FAQ](https://studio-neutrino.com/faq/)
- Workflow:
  - The input is MusicXML. Lyrics must be hiragana or katakana; English/alphabetic lyrics are not supported.
  - From MIDI, export the melody from a DAW and convert it to MusicXML in MuseScore. UtaFormatix converts other SVS projects.
  - A Windows GUI, Sig's "NEUTRINO調整支援ツール", lets you write scores from scratch.
  - The Windows build runs via Run.bat.
  — [NEUTRINO FAQ](https://studio-neutrino.com/faq/)

#### VOICEVOX (free, open-source editor; Japanese speech plus singing)
- The latest release is 0.25.2 (30 Apr 2026). Windows installers come in CPU, GPU/DirectML and GPU/CUDA variants; the CUDA zip is shown struck through. Earlier: 0.26.0-preview.0 pre-release (19 Apr), 0.25.1 (5 Jan), 0.25.0 (28 Oct, adds a song loop), 0.24.0 (25 Jun) [years inferred: 0.25.0 = 2025, 0.25.1 = 2026] — [GitHub: VOICEVOX releases](https://github.com/VOICEVOX/voicevox/releases)
- Runs on Windows, Mac and Linux; free for commercial and non-commercial use, subject to each character's terms. The "喋り声で歌えるハミング機能" (humming function) lets speaking voices sing — [VOICEVOX](https://voicevox.hiroshiba.jp/)
- Song editor milestones:
  - 0.16.0: song feature, with a Namine Ritsu song voice.
  - 0.17: save and undo.
  - 0.18: UST import and track selection on MIDI import.
  - 0.19: pitch editing.
  - 0.20: import of various project formats; experimental multitrack.
  - 0.21: multitrack becomes standard; export settings.
  - 0.22: mid-song BPM and time-signature changes.
  - 0.23: export to various project formats; lip-sync .lab files.
  - 0.25: loop.
  — [VOICEVOX update history](https://voicevox.hiroshiba.jp/update_history/)
- Editor licence: dual licence, LGPL v3 or a separate licence that does not require publishing source — [VOICEVOX repository](https://github.com/VOICEVOX/voicevox)

#### TuneLab (open source, MIT): young and extension-based
- "TuneLab is an extensible singing voice synthesis editor". Synthesis engines, project formats and effects come from `.tlx` extensions; it has built-in scripting and an AI agent.
- Releases "currently ship Windows x64 only", as an installer or a portable zip, and need the ".NET 8 Desktop Runtime". The binaries are unsigned, so Windows SmartScreen warns on first launch.
- The full manual exists only in Chinese; the UI is translated into Brazilian Portuguese (pt-BR, by @overdramatic).
— [TuneLab README](https://github.com/LiuYunPlayer/TuneLab)
- Releases:
  - v2.1.1 (13 Sep 2026, "Latest").
  - v2.1.0 (11 Sep): CLI/headless mode and an MCP entry point.
  - v2.0.0 (17 Aug 2026): rewrite with Effect and Instrument plugin types, AI assistant, Windows installer, MP3/FLAC/OGG and MIDI export.
  - v1.6.0 (29 Apr 2026): extension manager, 24/32-bit WAV export.
  - The release notes name no specific synthesis engine (DiffSinger, UTAU, VOICEVOX or other).
  — [TuneLab releases](https://github.com/LiuYunPlayer/TuneLab/releases) [years inferred]

#### DiffScope (OpenVPI): not usable yet
- "A free, professional singing-voice-synthesis editor powered by DiffSinger"; "This project is currently under development". Its progress list ticks the GUI shell, arrangement and piano-roll editors, phoneme/parameter editors and playback, but leaves "Integration of synthesis engine" unticked. Build from source only — [DiffScope project](https://github.com/diffscope/diffscope-project)

#### Commercial editors with a free tier: technical facts (pricing in earlier notes)
- Synthesizer V Studio 2: Windows 10/11, Intel Core i5 or equivalent AMD Ryzen, 4 GB RAM or more, 1 GB storage — [Dreamtonics Synthesizer V](https://dreamtonics.com/synthesizerv/)
- VoiSona: free editor for Windows and macOS (iOS/iPadOS as AUv3). The product page lists no PC specifications — [VoiSona Song](https://voisona.com/song/)
- ACE Studio: "the core features such as AI rendering and various AI tools require an internet connection as the AI services operate in the cloud" — [ACE Studio](https://acestudio.ai/)
- VOCALOID6 Editor: 31-day trial; needs Windows 11 22H2+ and 8 GB RAM (earlier notes) — [vocaloid.com trial](https://www.vocaloid.com/en/vocaloid6/trial/)
- Omnivocal Beta 1.2.5 (1 Apr 2026) comes with Cubase 15 and runs in Cubase/Nuendo only (earlier notes) — [Steinberg: Cubase 15 Downloads](https://o.steinberg.net/en/support/downloads/cubase_15.html)

### Inferences
- In October 2026, the free tools that are both maintained and usable on Windows are OpenUtau, NEUTRINO, VOICEVOX and TuneLab. OpenUtau is very active, but its "stable" build is 13 months old, so most new features (DAW bridge, package manager, DirectML fixes) are beta-only. NEUTRINO was updated in Sep 2026; VOICEVOX had a release in Apr 2026 and has a 0.26 preview. TuneLab is active, but which engine extensions it has is not documented in English. Classic UTAU is legacy, and DiffScope cannot synthesise yet.
- The GTX 1650 (4 GB) matters only for neural rendering:
  - optional DirectML in OpenUtau (DiffSinger) and in VOICEVOX's DirectML build;
  - CUDA in NEUTRINO, where 4 GB is at the bottom of the "4–6 GB is fine" range.
  - CPU rendering stays available everywhere.
  - That a GTX 1650 works with DirectML is an assumption (it is a DirectX 12-class GPU); the sources do not confirm it.
- An 8-core Ryzen 7 5800H very probably exceeds NEUTRINO's "PassMark 10000+" CPU recommendation. This is an assumption; no benchmark was checked.
- Choosing OpenUtau beta (0.1.569 or later) means installing the .NET 10 Desktop Runtime. It also means accepting that projects saved as .ustx 0.9 cannot be reopened in stable 0.1.565.

### Gaps
- OpenUtau's Windows asset names (installer vs zip, ARM64) could not be read because the asset lists did not load. No independent stability report on the 0.1.57x betas was found.
- TuneLab's available engine extensions (DiffSinger? UTAU? VOICEVOX?) and where to download them could not be established; the developer's GitHub repository list is blocked by robots.txt.
- NEUTRINO's formal system-requirements page and full EULA text were not read.
- VoiSona's current editor version and exact Windows requirements are not on the official product page.
- Other free engines (DeepVocal, Sinsy, Namine Ritsu's N-Editor, Mikoto Studio) were not researched beyond mentions on [Namine Ritsu's site](https://www.canon-voice.com/voicebanks/) and in the earlier notes.

## 2. What exactly is free in each option (voices, tracks, limits, watermark, time limit, account/online), and what licence governs commercial use of the rendered vocals?

### Takeaway
Only the open or free engines come with no time limit and no track cap:
- **OpenUtau**: no voices bundled; the rights to the output come from each voicebank's terms.
- **NEUTRINO**: 17 free voices; NEUTRINO itself puts no restriction on music use and crediting it is optional, but each character has its own terms.
- **VOICEVOX**: free, including commercial use, but you must credit VOICEVOX and follow per-character rules (Tohoku Zunko project voices need a credit line, or a ¥400,000 fee per character for uncredited commercial use).

Among the commercial products:
- **VoiSona**: two free Chis-A voices (Japanese and English) whose output may be used commercially without permission; other voices only play the first 10 seconds.
- **Synthesizer V Studio 2**: the free edition (post-trial "limited functionality", promoted as "Core") gives one vocal track, without ARA2 or vocal modes.
- **VOCALOID6**: only a 31-day trial.
- **ACE Studio**: a cloud account with unpublished free vocal limits.
- **Omnivocal**: free with Cubase 15, with explicit commercial rights.

### Cited Findings

#### OpenUtau / classic UTAU
- Software free under MIT — [OpenUtau repository](https://github.com/stakira/OpenUtau); no voicebank bundled — [OpenUtau wiki: FAQ](https://github.com/stakira/OpenUtau/wiki/FAQ)
- "File > Export Audio > Export wav Files" renders every track as a separate WAV; "Mixdown To Wav File" renders the mix; files go into an Export folder next to the .ustx — [OpenUtau wiki: Getting Started](https://github.com/stakira/OpenUtau/wiki/Getting-Started)
- For VOICEVOX voices inside OpenUtau, the wiki restates VOICEVOX's terms: commercial and non-commercial use are allowed. "Use of the created audio is subject to the terms and conditions of the respective audio library", and "Credit must be given to VOICEVOX when using this software" — [OpenUtau wiki: VOICEVOX support](https://github.com/stakira/OpenUtau/wiki/VOICEVOX-support)
- Classic UTAU is a free download with no licence text on its site — [UTAU official site](http://utau2008.xrea.jp/)

#### NEUTRINO
- Free: "NEUTRINOは、一般的な音楽制作およびオーディオ制作の範囲であれば、無料でダウンロード・利用いただけます。" (free to download and use for general music and audio production). Embedding NEUTRINO in a system, or using its audio inside an application, needs separate permission — [NEUTRINO FAQ](https://studio-neutrino.com/faq/)
- "2025年5月現在、すべての歌声ライブラリは無料でダウンロードおよびご利用いただけます。" (as of May 2025 all voice libraries are free) — [NEUTRINO FAQ](https://studio-neutrino.com/faq/)
- Commercial use: "楽曲制作など一般的な音声ファイルの利用用途ではNEUTRINO側には特に制約はありません。商用非商用問わずご利用いただけます。" (no particular restriction from NEUTRINO for music production, commercial or not). However, "キャラクター毎にライセンサー（権利保持者）が異なり" (each character has a different licensor), with separate terms for output audio, character and illustration — [NEUTRINO FAQ](https://studio-neutrino.com/faq/)
- Credit: "本ソフトウェアの使用報告・記載は任意となります。" (reporting or crediting the software is optional). Credit is also optional for NEUTRINO's own characters Merrow, Nakumo, Soma and Runo, whose audio may be used commercially. As of May 2025, songs can be distributed through TuneCore Japan, BIG UP!, JOYSOUND's うたスキミュージックポスト and Dwango's monetisation service — [NEUTRINO FAQ](https://studio-neutrino.com/faq/)
- For characters not on that list, a distributor may ask for "権利者からの許可を得ていることが確認できるもの" (proof of the rights holder's permission). For Tohoku Kiritan, Zundamon and Shikoku Metan, follow each project's guidelines and its commercial-sales flowchart — [NEUTRINO FAQ](https://studio-neutrino.com/faq/)

#### VOICEVOX
- Free for commercial and non-commercial use; follow each character's terms — [VOICEVOX](https://voicevox.hiroshiba.jp/)
- Credit to VOICEVOX is required; the software may not be redistributed. Other users of the audio you license must be bound by the same terms — [OpenUtau wiki: VOICEVOX support](https://github.com/stakira/OpenUtau/wiki/VOICEVOX-support), quoting the [VOICEVOX terms](https://voicevox.hiroshiba.jp/term/)
- Tohoku Zunko project voices on VOICEVOX (Tohoku Kiritan, Tohoku Itako, Shikoku Metan are named on the page):
  - Allowed: "商用、非商用ともにご利用いただけます。" (commercial and non-commercial use permitted).
  - Credit: "利用の際にはクレジット表記が必要になります。" (credit is required). Using them commercially without credit costs "１キャラクター毎に４０万円（＋消費税）" (¥400,000 + tax per character).
  - Prohibited: political or religious use, "information products", adult-entertainment businesses, antisocial forces.
  — [Tohoku Zunko project: VOICEVOX voice terms](https://zunko.jp/con_ongen_kiyaku.html)

#### VoiSona (Techno-Speech)
- The free editor includes 知声 (Chis-A, Japanese) and Chis-A [tʃíːseɪ] (English). Other libraries can be tried only up to "曲の先頭10秒" (the first 10 seconds of a song) before purchase — [VoiSona Song](https://voisona.com/song/)
- English Chis-A became free on 24 Apr 2026 and sings Japanese, English and Mandarin cross-lingually (earlier notes) — [Forest Watch (Impress)](https://forest.watch.impress.co.jp/docs/news/2089046.html)
- Chis-A guidelines (revised 10 Apr 2024):
  - Output audio: "商用／非商用、個人／法人を問わず、無償かつ当社許諾不要でご利用頂けます" (free and usable without permission, commercial or not, individual or corporate).
  - Embedding the voice in other instruments is prohibited.
  - Using the Chis-A *character* (name, visuals) needs permission for corporate use and for individual commercial use, except through listed services such as BIG UP!, TuneCore Japan and ROUTER.FM.
  - The guidelines state no credit requirement and contain no AI-training clause.
  — [VoiSona Chis-A guidelines (PDF)](https://voisona.com/static/pdf/chis-a_guidelines.pdf)

#### Synthesizer V Studio 2 (Dreamtonics)
- "This trial will run for 14 days and includes a curated selection of voices" (Windows .exe download) — [Dreamtonics free trials](https://dreamtonics.com/download-free-trials/)
- "When the trial period ends, the software simply reverts to limited functionality". Trial voices may send data to Dreamtonics servers, and "offline mode is not available"; each voice trial "ends automatically after seven days". "Synthesizer V Studio 2 Pro and all official Dreamtonics voices include commercial use licenses" — [Dreamtonics Synthesizer V](https://dreamtonics.com/synthesizerv/)
- Loopcloud (1 Jun 2026) calls "Synthesizer V Studio 2 Core" "the free edition of the software", with "the full Studio 2 interface and one vocal track". Studio Pro adds "unlimited tracks, ARA2 plugin support". Annual Loopcloud subscribers can claim it until 1 Jun 2027 — [Loopcloud blog](https://www.loopcloud.com/cloud/blog/5353-Get-Dreamtonics-Synthesizer-V-Studio-2-Core-Free-With-Your-Annual-Loopcloud-Subscription)
- BEAT magazine issue 10/26 bundles "Synthesizer V Studio 2 Core + one Voice of Choice" (post dated 8 Sep 2026) — [BEAT community](https://thebeatcommunity.com/2026/09/08/beat-magazine-offer-synthesizer-v-core-extra-voice-more-free/)
- Dreamtonics' own product and trial pages (read 8 Oct 2026) do not use the name "Core" — [Dreamtonics Synthesizer V](https://dreamtonics.com/synthesizerv/); [Dreamtonics free trials](https://dreamtonics.com/download-free-trials/)
- Earlier notes:
  - Fan wiki: the limited mode has one track and no AI Retakes, Vocal Modes or Mouth Opening — [SynthV Wiki](https://synthv.fandom.com/wiki/Synthesizer_V_Studio_2)
  - AHS: its v2 voices work in the free limited version, but without vocal styles.
  - The gen-1 "Synthesizer V Studio Basic" from AHS still exists: 3 tracks, and AHS's terms forbid commercial use of works made with it — [AHS Basic download](https://www.ah-soft.com/trial/synth-v.html)
- Kasane Teto's FAQ: the "Synthesizer V AI 重音テト ライト版" (Lite voice) permits no monetisation at all, "同人活動を含む一切の収益化を認められておりません" (not even doujin activity) — [Kasane Teto FAQ](https://kasaneteto.jp/guidelines/faq.html)

#### VOCALOID6 (Yamaha): trial only (earlier notes)
- 31-day full-feature trial. "VOCALOID6 Editor Lite" (2 tracks, standalone only) comes only with purchased voicebanks. A Hatsune Miku V6 "Special Trial" voice was released on 6 Jul 2026 for 31 days — [vocaloid.com trial](https://www.vocaloid.com/en/vocaloid6/trial/); [vocaloid.com news_42](https://www.vocaloid.com/en/news/news_42)

#### ACE Studio (Timedomain)
- The home page offers "Get Started Free" but publishes no free-tier terms. Its FAQ says "pre-made ACE Studio voices and instruments are royalty-free for commercial projects", and that cloud rendering requires internet — [ACE Studio](https://acestudio.ai/)
- The pricing page lists only paid tiers (Artist, Artist Pro, Enterprise/Team) and "over 100+ royalty-free voices across 8 languages" — [ACE Studio pricing](https://acestudio.ai/pricing/)
- "Other Registered Users: 100 Monthly Credits", refreshed on the 1st of each month. Credits pay for generative tools (Advanced Stem Splitter 60, Inspire Me 15, Add a layer 20, Video Composer 100, etc.); the article does not say whether vocal synthesis uses credits (updated 28 Jul 2026) — [ACE Studio support: AI Credit](https://support.acestudio.ai/article/147-ace-studio-ai-credit)
- SoundCloud Artist Pro users get a two-month ACE Studio trial and 20% off — [SoundCloud Help: ACE Studio](https://help.soundcloud.com/hc/en-us/articles/31508112524699-ACE-Studio)

#### Omnivocal Beta (inside Cubase 15) (earlier notes)
- Bundled at no extra cost. "All voice banks can be used freely, including for commercial music, without requiring any permission or credit from Yamaha or Steinberg"; the EULA forbids using it as AI-training material — [Yamaha Omnivocal](https://www.yamaha.com/en/about/business/music-connect/omnivocal/)

#### TuneLab
- Free and MIT-licensed; engines come from extensions, so output rights depend on the engine and voice used — [TuneLab README](https://github.com/LiuYunPlayer/TuneLab)

#### Summary table (free use as of 8 Oct 2026; sources are the bullets above)
| Tool | Cost / time limit | Voices free | Track / render limits | Account / online | Commercial use of rendered vocals |
|---|---|---|---|---|---|
| OpenUtau 0.1.565 / 0.1.57x beta | free, MIT, no time limit | none bundled (community banks) | none documented; WAV per track + mixdown | none documented | per voicebank terms |
| UTAU 0.4.19 | free | none needed for the editor | — | none documented | per voicebank terms |
| NEUTRINO Tau v3.2 | free | 17 libraries | MusicXML input, kana lyrics | none documented (Colab variant is online) | allowed by NEUTRINO, credit optional; per-character terms |
| VOICEVOX 0.25.2 | free | singing and humming characters | multitrack song editor | none documented | allowed; credit "VOICEVOX" + character terms |
| VoiSona | free editor | Chis-A JP + Chis-A EN | other voices: first 10 s only | login exists; requirement unverified | Chis-A audio free, no permission; character name/visual restricted |
| Synthesizer V Studio 2 free ("limited"/"Core") | free after 14-day trial; Core via promos | trial voices 7 days; Core promos add 1 voice | 1 vocal track; no ARA2, no vocal modes | trial voices online; Dreamtonics account (AHS) | Pro + official voices licensed; free-mode terms unconfirmed |
| VOCALOID6 Editor | 31-day trial | trial voicebanks | full during trial | — | moot after trial |
| ACE Studio | free account | not published | not published | cloud, account | pre-made voices royalty-free (free-tier scope unclear) |
| Omnivocal Beta | free with Cubase 15 | 2 (Female, Male) | one voice per instrument track | EULA consent | yes, no credit needed |
| TuneLab 2.1.1 | free, MIT | depends on extension | — | none documented | depends on engine/voice |

### Inferences
- Truly "free forever, no caps" applies only to OpenUtau/UTAU, NEUTRINO and VOICEVOX (and TuneLab once an engine is installed). The commercial products' free tiers are capped (VoiSona voices, SynthV tracks), time-limited (VOCALOID6) or opaque and online-only (ACE Studio).
- For an individual hobbyist who wants to stream or sell songs, these carry the least paperwork:
  - Omnivocal: no credit.
  - VoiSona Chis-A, used as a voice without the character: no permission, no credit.
  - NEUTRINO's own characters: credit optional.
  - Kasane Teto UTAU: individual sales and streaming allowed, no credit (see Q3).
  - VOICEVOX and Tohoku-family voices: they require a credit line in every release.
- "Synthesizer V Studio 2 Core" looks like the marketing name for the free, one-track edition, distributed through partners (Loopcloud, BEAT). Dreamtonics' own pages only speak of "limited functionality". Either way, Synthesizer V's free route is a taster: one track, and voices that are paid or time-limited.

### Gaps
- Whether vocals rendered in Synthesizer V's free or limited mode ("Core") carry the same commercial licence as Pro is not stated by Dreamtonics.
- ACE Studio's free-account limits on vocal rendering and export (watermark, duration, credits) are unpublished.
- Whether VoiSona needs a signed-in account or a connection for its free voices, and whether English Chis-A follows the same guidelines PDF as Japanese 知声, were not confirmed.
- No watermark information was found for any free tool. The only watermark mention is Omnivocal's EULA ban on altering watermarks (earlier notes).
- What the VOCALOID6 trial restricts (saving/exporting) remains unconfirmed (gap carried over from the earlier notes).

## 3. Which free voicebanks are the most popular and best quality, and what are their terms of use?

### Takeaway
Kasane Teto's official UTAU libraries (including a ready-made OpenUtau set and an English CVVC bank) are the only free, legal way to use one of today's most famous virtual singers, and her terms let individuals sell, stream and monetise songs without credit or notice. For more realistic free voices, the main options are:
- Namine Ritsu: UTAU, ENUNU and DiffSinger versions, all free on her site.
- NEUTRINO's 17 free singers, including Tohoku Kiritan, Zundamon and Kotonoha Akane/Aoi.
- VOICEVOX's singing characters, such as Zundamon.
- VoiSona's Chis-A, in Japanese and English.

Hatsune Miku has no free voice; she is available only through paid products or 31–39-day trials.

### Cited Findings

#### Kasane Teto (UTAU/OpenUtau): free, official
- Ten free official UTAU libraries (2010–2024), including English CVVC (2015) and an "OpenUTAU Japanese Library Set" (23 Mar 2024) (earlier notes) — [kasaneteto.jp UTAU](https://kasaneteto.jp/utau/)
- Voice terms (issued 1 Apr 2011, last revised 3 Apr 2023):
  - Free for individuals and corporations for non-commercial activity.
  - Individuals may sell their own songs at events or online (BOOTH).
  - Paid distribution on streaming services by individuals "今の所商用利用に当たりません" (currently does not count as commercial use); the same applies to video ad revenue.
  - Commercial use of the library needs permission from Crypton Future Media (Piapro desk).
  - No credit is required.
  - Redistributing a UTAU voicebank, whole or in part, modified or not, is prohibited; your own frq and oto.ini edits may be shared.
  — [Kasane Teto voice terms](https://kasaneteto.jp/guidelines/voice.html)
- FAQ:
  - Individuals may release songs through TuneCore Japan, ROUTER.FM, BIG UP!, KARENT, narasu, Eggs Pass and NRC, including Teto's visual and name: "ご自由にどうぞ！ご連絡・ご報告不要です。" (go ahead, no contact or report needed).
  - YouTube/Niconico ad revenue: "個人であればOKです！報告義務もありません。" (fine for individuals, no reporting).
  - "Commercial use" means company business (ads, label releases, game music). Using only the voice without name or visual counts as plain audio material, so "重音テト公式の許諾は必要ありません" (no official permission needed).
  - Redistribution of the library is "原則禁止" (prohibited in principle), and this includes modified versions and anything trained into AI.
  - AI training on Teto's voice is OK "個人で楽しむ範囲" (for personal enjoyment), but never on the Synthesizer V or VOICEPEAK data.
  — [Kasane Teto FAQ](https://kasaneteto.jp/guidelines/faq.html)

#### Namine Ritsu (Canon): free UTAU, ENUNU/NNSVS and DiffSinger
- The official site offers:
  - UTAU banks: キレ (Kire, presented on the page as her best-known bank), 強, 通常, Eve (CVVC) and 眩＆麗 (CVVC).
  - ENUNU/NNSVS "CRISSCROSS" five-style models. #4130 is recommended; #4230 is "for experts". They need SimpleEnunu 0.4.0+.
  - A DiffSinger voicebank, Ver.1.0.1, for OpenUtau.
  - N-Editor v0.30.0, an editor with wavehax vocoder support.
  - Links to DeepVocal, Sinsy, ACE Studio and VOICEVOX versions.
  — [Namine Ritsu voicebanks (canon-voice.com)](https://www.canon-voice.com/voicebanks/)
- The OpenUtau wiki uses the Ritsu CRISSCROSS model as its reference example for multi-style ENUNU banks — [OpenUtau wiki: ENUNU NNSVS Support](https://github.com/stakira/OpenUtau/wiki/ENUNU-NNSVS-Support)
- VOICEVOX added a Namine Ritsu song voice in 0.16.0 — [VOICEVOX update history](https://voicevox.hiroshiba.jp/update_history/)

#### NEUTRINO's free singers
- 17 free v3 "Tau" libraries (about 345–349 MB each): Merrow, Reina, Nakumo, Soma, Runo, Kotonoha Akane, Kotonoha Aoi, Yogatari Tobari, Tohoku Itako, Tohoku Zunko, Tohoku Kiritan, Shikoku Metan, Zundamon, Oedo Chanko, Seven, Yoko, JSUT — [NEUTRINO downloads](https://studio-neutrino.com/downloads/)
- Terms: NEUTRINO's own characters may be used commercially with optional credit; Tohoku-family characters follow their projects' guidelines (see Q2) — [NEUTRINO FAQ](https://studio-neutrino.com/faq/)

#### VOICEVOX singers
- The song feature launched in v0.16.0 (31 Jan 2024) with Zundamon, Shikoku Metan, Kasukabe Tsumugi, Amehare Hau and Namine Ritsu (earlier notes) — [Forest Watch (Impress)](https://forest.watch.impress.co.jp/docs/news/1567478.html). Humming voices were added for many more characters in 0.16–0.18 — [VOICEVOX update history](https://voicevox.hiroshiba.jp/update_history/)
- Credit and Tohoku-family terms as in Q2 — [Tohoku Zunko project: VOICEVOX voice terms](https://zunko.jp/con_ongen_kiyaku.html)

#### Other free voices (earlier notes)
- VoiSona Chis-A (JP and EN), terms in Q2 — [VoiSona Chis-A guidelines (PDF)](https://voisona.com/static/pdf/chis-a_guidelines.pdf)
- Adachi Rei: free UTAU bank (2019) and a DiffSinger port (3 May 2025) — [Vocaloid Wiki: Adachi Rei](https://vocaloid.fandom.com/wiki/Adachi_Rei)
- Eleanor Forte Lite (Synthesizer V, English): free since 30 Jul 2020; licence allows individual commercial use under US$1,000 — [SynthV Wiki: Eleanor Forte](https://synthv.fandom.com/wiki/Eleanor_Forte)

#### Hatsune Miku: no free voice (earlier notes)
- The cheapest legal Miku is the VOCALOID6 voicebank (US$78 with Editor Lite). Free options are trials only: "Hatsune Miku V6 Voicebank Special Trial" (31 days, from 6 Jul 2026) and Hatsune Miku NT (39-day trial) — [vocaloid.com news_42](https://www.vocaloid.com/en/news/news_42); [SONICWIRE Hatsune Miku NT](https://sonicwire.com/product/virtualsinger/special/mikunt)

### Inferences
- Teto on OpenUtau is the only zero-cost, permanent and legal way to make songs with one of the most famous virtual singers. Miku needs money or a 31–39-day trial.
- Because Teto's FAQ forbids redistributing "anything trained into AI", any downloadable unofficial "Teto DiffSinger/AI" model circulating online is outside the official terms. The legal free Teto is the official UTAU set.
- Expected quality (inference; no measured comparison was found): the neural voices (NEUTRINO libraries, DiffSinger/ENUNU banks such as Namine Ritsu, VoiSona Chis-A) sound more natural with less tuning than concatenative UTAU banks. Teto's UTAU banks give the classic "UTAU sound" heard in older hits.
- Licensing friendliness for a hobbyist releasing on Spotify or YouTube:
  - Teto, Chis-A (voice-only) and NEUTRINO's own characters: no credit needed.
  - VOICEVOX and Tohoku-family voices: credit lines needed.

### Gaps
- No curated, up-to-date list or popularity ranking of free DiffSinger voicebanks (Japanese or English) was found. The [vocalsynth wiki DiffSinger page](https://vocalsynth.fandom.com/wiki/DiffSinger) lists none; English free DiffSinger banks remain unresearched.
- Namine Ritsu's terms-of-use page and the terms of Kasukabe Tsumugi, Amehare Hau and Kotonoha Akane/Aoi were not read.
- No official Kasane Teto DiffSinger or NEUTRINO voice was found.

## 4. How do these tools connect to Cubase LE/AI 15, FL Studio 2024 and REAPER (VST3/CLAP, ARA2, bridges, ReWire, MIDI/MusicXML/USTX/SVP, WAV drag-and-drop)?

### Takeaway
Most free engines have no DAW plug-in. The universal route is: write in the editor, export WAV, drag it into the DAW at the same BPM, using MIDI/MusicXML/UST files to move melodies in.

Two plug-in routes exist:
- **OpenUtau bridge (new)**: since 3 Oct 2026 the OpenUtau beta (0.1.571+) has an official DAW-integration API plus a separate VST3/CLAP "openutau-vst-bridge". It streams rendered parts onto the DAW timeline and follows the DAW's playhead, but has no tempo-map sync and is untested in hosts.
- **Commercial plug-ins**: VoiSona (VSTi/AU), Synthesizer V and VOCALOID6 (VST3, ARA2 in paid editions) and ACE Bridge.

ARA2 does not help this user in two of his three DAWs: Yamaha says Cubase AI has no ARA2 (and no VOCALOID transport link), and FL Studio still had no ARA in April 2026. REAPER is the only one of his hosts with ARA2 (since 2019) and with both CLAP and VST3. Omnivocal remains Cubase-only.

### Cited Findings

#### OpenUtau ↔ DAW bridge (new, beta only)
- PR #2369, merged into `openutau:master` on 6 Sep 2026, adds a DAW-integration API:
  - OpenUtau sends the project document, track configuration and rendered part audio to the DAW.
  - The DAW sends back transport position, playing state and tempo.
  - Audio travels as raw 44.1 kHz stereo float32, pre-fader, and the DAW handles mixing.
  - The API shipped "dormant", with the UI following in PR #2376.
  — [OpenUtau PR #2369](https://github.com/stakira/OpenUtau/pull/2369)
- 0.1.571 Beta (3 Oct 2026) exposes it in the UI, "with an in-app bridge guide that detects the install" and "can install with one click" (credited to @KakaruHayate; PRs #2369, #2376, #2476) — [GitHub: OpenUtau releases](https://github.com/stakira/OpenUtau/releases)
- What the bridge plug-in is and how it syncs:
  - "A thin plugin that puts OpenUtau's rendered audio on the DAW timeline"; editing stays in OpenUtau.
  - Formats: CLAP, wrapped to VST3 with clap-wrapper; no AU; no AAX (Pro Tools out of scope).
  - Hosts the formats reach (listed as reachable, not tested): Bitwig, Reaper, FL Studio, Studio One and Qtractor via CLAP; Ableton Live and Cubase/Nuendo via VST3.
  - Transport: the playhead goes one way only, DAW → OpenUtau (on state changes, every 100 ms while playing).
  - Tempo: the DAW tempo is reported and OpenUtau warns on mismatch, but there is "no tempo-map sync".
  - Tracks: one plug-in instance per DAW track, with an "OpenUtau Track" parameter choosing which OpenUtau track it plays.
  - Mixing: OpenUtau's volume, pan and mute are ignored; the DAW mixes.
  - Licence MPL-2.0. Build instructions are Windows/MSVC; the Releases section is empty and the README lists no prebuilt binaries.
  — [openutau-vst-bridge (GitHub)](https://github.com/KakaruHayate/openutau-vst-bridge)

#### File interchange (melody in, audio out)
- OpenUtau:
  - Imports tracks from .ustx, .ust and .vsqx; MIDI via File > Import MIDI; audio from .wav, .mp3, .ogg and .flac.
  - Exports per-track .ust files, per-track WAV and a WAV mixdown.
  — [OpenUtau wiki: Getting Started](https://github.com/stakira/OpenUtau/wiki/Getting-Started)
  - MusicXML import was added in PR #1152 and later improved (slurs, ties, multisyllabic words, PR #1753); .ufdata import in PR #790 — [OpenUtau wiki: Release Notes](https://github.com/stakira/OpenUtau/wiki/Release-Notes)
- VOICEVOX song: imports UST and MIDI (track selectable) since 0.18 and "様々な形式のプロジェクトファイル" (various project formats) since 0.20; exports various project formats since 0.23 — [VOICEVOX update history](https://voicevox.hiroshiba.jp/update_history/). Exports WAV (earlier notes) — [Forest Watch (Impress)](https://forest.watch.impress.co.jp/docs/news/1567478.html)
- NEUTRINO: MusicXML only. Make a single-part MIDI melody in the DAW, then use MuseScore to produce MusicXML, or convert other SVS projects with UtaFormatix — [NEUTRINO FAQ](https://studio-neutrino.com/faq/)
- VoiSona: input via MIDI through the DAW, or MusicXML files — [VoiSona Song](https://voisona.com/song/)
- TuneLab: WAV (24/32-bit), MP3, FLAC and OGG audio export plus MIDI export — [TuneLab releases](https://github.com/LiuYunPlayer/TuneLab/releases)
- Converters:
  - UtaFormatix3 (Apache-2.0) imports .vsqx, .vpr, .vsq, VOCALOID/standard .mid, .ust, .ustx, .ccs, MusicXML, .svp, .s5p, .dv, .ppsf (NT), .tssln and .ufdata, and exports most of them. It keeps tracks, notes, tempo and time signatures, and pitch for some formats — [UtaFormatix3 (GitHub)](https://github.com/sdercolin/utaformatix3)
  - LibreSVIP (MIT) is "a cross-platform and universal converter for many Singing Voice Synthesis (aka SVS) project formats" — [LibreSVIP (GitHub)](https://github.com/SoulMelody/LibreSVIP)

#### VOICEVOX as a plug-in: not released
- The official VOICEVOX organisation has a `voicevox_vst` repository described only as "VOICEVOXエディタのVSTプラグイン。" (a VST plug-in for the VOICEVOX editor). Its Releases section was empty on 8 Oct 2026 — [VOICEVOX/voicevox_vst](https://github.com/VOICEVOX/voicevox_vst)

#### Plug-in and ARA status of the commercial free tiers
- VoiSona can be added to a DAW as "VSTiプラグイン、もしくはAudio Units (AU)プラグイン" (VSTi or AU; AUv3 on iPad) — [VoiSona Song](https://voisona.com/song/). ARA2 support per the fan wiki (earlier notes) — [CeVIO & VoiSona Wiki: VoiSona](https://cevio.fandom.com/wiki/VoiSona)
- Synthesizer V: the free edition ("Core") has one track, and Pro "adds unlimited tracks, ARA2 plugin support" — [Loopcloud blog](https://www.loopcloud.com/cloud/blog/5353-Get-Dreamtonics-Synthesizer-V-Studio-2-Core-Free-With-Your-Annual-Loopcloud-Subscription). The trial page lists VST3, AU, AAX and ARA under the paid versions — [Dreamtonics free trials](https://dreamtonics.com/download-free-trials/). Fan wiki: in limited mode "plug-ins present but restricted" (earlier notes) — [SynthV Wiki](https://synthv.fandom.com/wiki/Synthesizer_V_Studio_2)
- VOCALOID6 Editor: VST3 with ARA2; Editor Lite is standalone only (earlier notes) — [vocaloid.com specs](https://www.vocaloid.com/en/vocaloid6/specs/)
- ACE Studio: ACE Bridge "VST3, AU, AAX supported"; "With ARA link mode, you can sync playback and tempo at all times" — [ACE Studio](https://acestudio.ai/)
- Omnivocal: Cubase 15/Nuendo 15 only, on instrument tracks only (not the VSTi rack or MIDI tracks). In other DAWs it shows "Omnivocal Beta Is Not Available in This DAW" (earlier notes) — [Steinberg Help Center](https://helpcenter.steinberg.de/hc/en-us/articles/30879147782034-Yamaha-Omnivocal-Beta-shows-an-error-Omnivocal-Beta-Is-Not-Available-in-This-DAW)

#### Host capabilities
- **Cubase AI and ARA (Yamaha):** "As of October 2022, Cubase AI does not have an ARA2 function. Please consider purchasing Cubase Pro/Artist." — [VOCALOID FAQ 654](https://vocaloid.com/en/support/faq/654). Yamaha's guide for Cubase AI/LE/Elements says "Cubase AI doesn't support ARA2", and that VOCALOID6 transport (play/stop) is not linked with Cubase AI projects; it loads as "VOCALOID VSTi" on an instrument track. Transport and tempo linking are a Pro/Artist feature — [vocaloid.com guide ln6203](https://www.vocaloid.com/en/learn/ln6203)
- **Cubase LE/AI track limits:** the most recent official-looking figures found are for **Cubase 11** (Shimamura comparison table, 7 Apr 2021):

  | | Audio tracks | MIDI tracks | Instrument tracks |
  |---|---|---|---|
  | Cubase AI 11 | 32 | 48 | 16 |
  | Cubase LE 11 | 16 | 24 | 8 |

  The same table notes that "LE、AIはVSTインストゥルメントを大量に立ち上げる事は出来ません" (LE and AI cannot run large numbers of VST instruments) — [Shimamura Music (2021)](https://www.shimamura.co.jp/shop/kinshicho-p/?p=12474)
- **FL Studio:**
  - FL Studio 2024 "also brings support for the CLAP plugin format" (article of 2 Jul 2024) — [MusicRadar](https://www.musicradar.com/news/fl-studio-2024-update)
  - No ARA: the Image-Line forum thread "Request for ARA2 Support for Melodyne in FL Studio" is still open; its latest post (6 Apr 2026, a user) says ARA "will never" come. A Jan 2025 user post attributes the delay to Image-Line's audio-engine rewrite. No staff confirmation of any ARA release was found — [Image-Line forum](https://forum.image-line.com/viewtopic.php?p=2035826)
  - FL Studio is among the DAWs Dreamtonics names as compatible with the Synthesizer V plug-in (earlier notes) — [Dreamtonics announcement](https://dreamtonics.com/?p=1945)
- **REAPER:** ARA 2 with Melodyne since early 2019 (per headlines: "Melodyne and Reaper Are Now Able To Communicate Via ARA 2") — [audioXpress](https://audioxpress.com/news/melodyne-and-reaper-are-now-able-to-communicate-via-ara-2); [REAPER Blog, March 2019](https://reaper.blog/2019/03/melodyne-ara/). The OpenUtau bridge lists Reaper as reachable via CLAP — [openutau-vst-bridge](https://github.com/KakaruHayate/openutau-vst-bridge)

### Inferences
- Cubase LE/AI 15:
  - Treat ARA as unavailable. The Yamaha statements are from 2022 (Cubase 12 era), but nothing found says AI/LE gained ARA since.
  - VoiSona, Synthesizer V and VOCALOID6 can still be used as ordinary VST3 instruments (no ARA, no transport link for VOCALOID6), or as standalone apps feeding WAV files.
  - Each such voice, and each Omnivocal voice, uses one instrument track. If the Cubase 11 limits still apply, that is about 8 vocal instrument tracks in LE and 16 in AI.
- FL Studio 2024 (24.2): VST3 and CLAP plug-ins work, but ARA modes (SynthV Pro ARA, VOCALOID6 ARA, VoiSona ARA, ACE "ARA link mode") are unavailable. The OpenUtau bridge should load via CLAP (FL 2024+), but nobody has reported testing it.
- REAPER 7.61 is the best host on this machine: ARA2 for the commercial editors, and both CLAP and VST3 for the OpenUtau bridge.
- The OpenUtau bridge is attractive (edit in OpenUtau, hear it in the DAW at the right position) but immature:
  - Beta-only, one-way transport, no tempo-map sync.
  - Only a source repository is documented, while the release notes claim one-click install from inside OpenUtau.
  - The safest way to use it is with a fixed project tempo identical in both programs.
- Integration matrix (derived from the cited facts; "WAV" = render in the editor, then drag the file into the DAW):

| Tool | Cubase LE/AI 15 | FL Studio 2024 (24.2) | REAPER 7.61 |
|---|---|---|---|
| OpenUtau stable 0.1.565 | WAV; MIDI/MusicXML/UST in | WAV | WAV |
| OpenUtau beta 0.1.571+ bridge | VST3 bridge (untested) | CLAP or VST3 bridge (untested) | CLAP/VST3 bridge (untested) |
| NEUTRINO | WAV only (MusicXML in) | WAV only | WAV only |
| VOICEVOX | WAV only (VST not released) | WAV only | WAV only |
| VoiSona (free Chis-A) | VSTi, no ARA | VSTi, no ARA | VSTi + ARA2 (per wiki) |
| SynthV Studio 2 free/"Core" | plug-in restricted, no ARA2 | same | same (ARA needs Pro) |
| VOCALOID6 trial | VST3, no ARA, no transport link | VST3, no ARA | VST3 + ARA2 |
| ACE Studio (free account) | ACE Bridge VST3, no ARA | ACE Bridge VST3, no ARA | ACE Bridge + ARA link |
| Omnivocal Beta | native (instrument track) | not available | not available |
| UTAU 0.4.19 / TuneLab | WAV | WAV | WAV |

### Gaps
- No hands-on report of openutau-vst-bridge in Cubase (LE/AI), FL Studio 24.2 or REAPER 7.61 was found. Also unknown: whether it registers as an instrument or an effect (which matters for LE/AI instrument-track limits) and where the "one-click install" gets its binary.
- Cubase 15 LE/AI track limits and ARA status were not found on a current Steinberg page; the comparison page is JavaScript-rendered. The figures above are Cubase 11 (2021) and Yamaha's 2022 statements.
- ReWire was not researched; none of the free editors' pages read mention ReWire.
- Whether VoiSona's Windows plug-in is VST3 or VST2 ("VSTi"), and whether ARA2 works in REAPER, are not confirmed on official pages.
- Whether Synthesizer V's free edition can run as a plug-in at all (vs standalone only) is not stated by Dreamtonics.

## 5. Can any engine or voicebank sing in Brazilian Portuguese (official or community)?

### Takeaway
Among free tools, only the OpenUtau ecosystem sings Brazilian Portuguese, and it is entirely community-made:
- a built-in "PT-BR CVC" phonemizer;
- the BRAPA phonetic alphabet;
- community DiffSinger/UTAU phonemizer plug-ins;
- Brazilian voicebanks such as those of the Studio Pomar collective.

No famous character sings Portuguese officially. Among commercial tools, only ACE Studio lists Portuguese as a released language (variant unconfirmed), and Synthesizer V has experimental Brazilian Portuguese only in the 2.3.0 technical preview (earlier notes). NEUTRINO, VOICEVOX, VoiSona, Omnivocal and VOCALOID6 have none.

### Cited Findings
- OpenUtau's built-in "PT-BR CVC (Brazilian Portuguese CVC)" phonemizer is "made with BRAPA conotation", uses a built-in G2P dictionary, and its main accent is "Neutral". It accepts Portuguese words (`leite`), words plus a phonetic hint (`leite[l e y t e]`), or hints only — [OpenUtau wiki: Phonemizers](https://github.com/stakira/OpenUtau/wiki/Phonemizers)
- BRAPA is "A Brazilian Portuguese Phonetic Alphabet made for Synthesizers", based on Arpabet and avoiding special characters; its phoneme index can be adapted to regional accents; authors @nachokuma and @overdramatic — [Team-BRAPA/BRAPA](https://github.com/Team-BRAPA/BRAPA)
- Community DiffSinger phonemizer "DiffSinger BRAPA Phonetic (xiao)": a DLL for OpenUtau's Plugins folder for "bancos de voz em Português Brasileiro (BRAPA / Saturno)". It needs no G2P dictionary because phonemes are typed directly; MIT licence — [openutau-plugin-ptbr-brapa-phonetic](https://github.com/dorayakito/openutau-plugin-ptbr-brapa-phonetic)
- Community set of 10 PT-BR phonemizers:
  - BRAPA CVVC, VCV and CV;
  - IPEA CVVC with G2P;
  - X-SAMPA CVVC;
  - F-SAMPA/Brigadeiro;
  - NUBLADO;
  - CATIPA (based on the Junei Aiden voicebank);
  - CATIPA DiffSinger and X-SAMPA DiffSinger.
  - They are distributed as C# source that must be compiled into OpenUtau.
  — [Phonemizers-PTBR README](https://github.com/dorayakito/Phonemizers-PTBR/blob/main/README.md)
- Studio Pomar, "Um coletivo de voicebanks e ferramentas livres para UTAU e OpenUTAU" (a collective of voicebanks and free tools for UTAU and OpenUTAU), lists these voicebanks; the page states neither prices nor terms:
  - VIICTOR: Brazilian, since 2013, multilingual (30+ languages).
  - YOHJI: since 2010.
  - EDDIE: "o primeiro banco de voz configurado especificamente para o português brasileiro, lançado em 2012" (the first voicebank configured specifically for Brazilian Portuguese, released 2012).
  - MIZUKI: UTAU and DiffSinger.
  - KODAMA KITO: since 2026.
  - APOLLYO XII: since 2025.
  — [Studio Pomar](https://studiopomar.github.io/)
- TuneLab's interface has a pt-BR translation by @overdramatic (also a BRAPA author) — [TuneLab README](https://github.com/LiuYunPlayer/TuneLab)
- Commercial (earlier notes):
  - Synthesizer V 2.3.0 Technical Preview (22 May 2026) adds experimental Brazilian Portuguese for updated Dreamtonics v2 voices; still preview-only in early Oct 2026 — [Dreamtonics forum](https://forum.dreamtonics.com/t/synthesizer-v-studio-2-pro-2-3-0-technical-preview/8046). Wikipedia lists "Beta: French, German, Brazilian Portuguese" — [Wikipedia: Synthesizer V](https://en.wikipedia.org/wiki/Synthesizer_V)
  - ACE Studio 2.0 lists Portuguese among eight singing languages — [Sound On Sound](https://www.soundonsound.com/news/ace-studio-20-timedomain). Its own pricing page says only "8 languages" without naming them — [ACE Studio pricing](https://acestudio.ai/pricing/)
- No Portuguese:
  - NEUTRINO accepts only kana lyrics, so "英語や英字の歌詞" (English/alphabetic lyrics) are unsupported — [NEUTRINO FAQ](https://studio-neutrino.com/faq/)
  - OpenUtau's VOICEVOX phonemizers are Japanese and English→Japanese only — [OpenUtau wiki: VOICEVOX support](https://github.com/stakira/OpenUtau/wiki/VOICEVOX-support)
  - VoiSona is JA/EN/ZH; Omnivocal is EN/JA; VOCALOID6 is JA/EN/ZH (earlier notes).
- Fan ports of Adachi Rei for UTAU/DiffSinger are listed with many languages, including Portuguese (earlier notes) — [Vocaloid Wiki: Adachi Rei](https://vocaloid.fandom.com/wiki/Adachi_Rei)

### Inferences
- The free route to Portuguese lyrics today is OpenUtau with a Brazilian UTAU bank (CVC/VCV/CVVC) and the built-in PT-BR CVC phonemizer, or with a PT-BR DiffSinger bank and a community BRAPA phonemizer. Expect hobbyist-level quality and some manual phoneme editing.
- Famous characters (Teto, Miku, Zundamon) can only approximate Portuguese with Japanese or English phonemes typed by hand. Nasal vowels and "lh/nh" sounds will be weak.
- Synthesizer V's PT-BR preview is the most promising "AI" Portuguese, but it needs paid Pro features and Dreamtonics' own v2 voices, so it is not a free option.

### Gaps
- No list of downloadable PT-BR DiffSinger voicebanks, with links and licences, was found. The "Saturno" bank named by the BRAPA phonemizer was not located.
- Studio Pomar's voicebank terms, free status and download links were not visible on the page read. The Junei Aiden UTAU bank (an itch.io page surfaced in search) was not opened.
- No quality review of Portuguese singing in any engine was found.
- Whether ACE Studio's Portuguese is Brazilian or European remains unconfirmed.

## 6. Bottom line: which single free option gives the best quality-for-effort today, and what are the trade-offs between the top three?

### Takeaway
For this user, the best single free option is **OpenUtau**: stable 0.1.565, or beta 0.1.571+ if he wants to try the new DAW bridge. He should use it with Kasane Teto's official free library set and, for more natural results, free neural banks such as Namine Ritsu's DiffSinger or ENUNU models. It is the only free tool that combines all of these:
- a famous character;
- no track or time limits;
- release-friendly terms;
- a Brazilian Portuguese phonemizer;
- a route into all three of his DAWs (WAV everywhere, plug-in bridge in beta).

The runners-up:
- **VoiSona**: the free Chis-A voice in Japanese and English gives AI-quality output, a normal plug-in and clean commercial terms, but only one character and no Portuguese.
- **NEUTRINO**: 17 free neural Japanese singers, including Kiritan and Zundamon, but only Japanese kana lyrics, MusicXML input and no DAW plug-in.

Omnivocal is the zero-setup choice inside Cubase but only sketch-quality, English/Japanese. Synthesizer V's free edition and the VOCALOID6/Miku trials are tasters, not free solutions.

### Cited Findings
- OpenUtau: free MIT software with no bundled voice — [OpenUtau wiki: FAQ](https://github.com/stakira/OpenUtau/wiki/FAQ). Active beta development with a DAW bridge since 3 Oct 2026 — [GitHub: OpenUtau releases](https://github.com/stakira/OpenUtau/releases); [openutau-vst-bridge](https://github.com/KakaruHayate/openutau-vst-bridge). DiffSinger with optional DirectML GPU acceleration — [OpenUtau wiki: DiffSinger support](https://github.com/stakira/OpenUtau/wiki/DiffSinger-support). PT-BR phonemizer — [OpenUtau wiki: Phonemizers](https://github.com/stakira/OpenUtau/wiki/Phonemizers)
- Teto: official free UTAU and OpenUtau libraries (earlier notes) — [kasaneteto.jp UTAU](https://kasaneteto.jp/utau/). Individuals may sell, stream and monetise with no report or credit — [Kasane Teto FAQ](https://kasaneteto.jp/guidelines/faq.html)
- VoiSona: free Chis-A JP and EN; other voices limited to 10-second previews; VSTi/AU plug-in — [VoiSona Song](https://voisona.com/song/). Output usable commercially without permission — [VoiSona Chis-A guidelines (PDF)](https://voisona.com/static/pdf/chis-a_guidelines.pdf)
- NEUTRINO: all 17 voice libraries free; no restriction from NEUTRINO for music use; kana-only MusicXML; GPU recommended (4–6 GB VRAM fine) — [NEUTRINO FAQ](https://studio-neutrino.com/faq/); [NEUTRINO downloads](https://studio-neutrino.com/downloads/)
- Omnivocal (earlier notes): Sound On Sound on final-mix use: "Right now, I think the answer is 'probably not'!" MusicRadar: "It's certainly not going to compete with something like Dreamtonics Synthesiser V or Ace Studio in terms of its expressiveness, realism and flexibility." Forum users in Aug 2026 still recommend Synthesizer V Studio 2 Pro for serious work — [Sound On Sound](https://www.soundonsound.com/techniques/cubase-15-exploring-omnivocal); [MusicRadar](https://www.musicradar.com/music-tech/daws/steinberg-cubase-15-review); [Steinberg forum](https://forums.steinberg.net/t/omnivocal-beta/1039571)
- Synthesizer V's free edition: one vocal track and no ARA2 — [Loopcloud blog](https://www.loopcloud.com/cloud/blog/5353-Get-Dreamtonics-Synthesizer-V-Studio-2-Core-Free-With-Your-Annual-Loopcloud-Subscription). Trial voices last 7 days and need online access — [Dreamtonics Synthesizer V](https://dreamtonics.com/synthesizerv/)

### Inferences
- Ranking for "best free quality-for-effort" on this machine (judgement from the cited facts; no hands-on test):
  1. **OpenUtau + Teto UTAU (+ DiffSinger/ENUNU banks)**
     - Pros: unlimited, legal famous voice, huge community, Portuguese possible, DAW bridge coming.
     - Cons: UTAU banks need manual tuning for a natural sound; DiffSinger/ENUNU setup takes extra steps (vocoder package, beta channel, ENUNU server); the bridge is beta.
  2. **VoiSona with free Chis-A (JP/EN)**
     - Pros: best out-of-the-box realism among the truly free voices, standard plug-in, the simplest commercial terms.
     - Cons: one character, no Portuguese, other voices cost ¥880/month or more (earlier notes), no ARA in Cubase LE/AI or FL.
  3. **NEUTRINO (Kiritan, Zundamon, Kotonoha sisters, etc.)**
     - Pros: high-quality free Japanese neural singing with many recognisable characters.
     - Cons: Japanese kana only, MusicXML workflow (DAW → MIDI → MuseScore → MusicXML → WAV), no plug-in, the GTX 1650's 4 GB is at the low edge.
  - Honourable mention: **Omnivocal**, already installed. It is the fastest way to hear a melody sung inside Cubase, with commercial use allowed, but it is generic and English/Japanese only, lacks famous characters, and is not usable in FL Studio or REAPER.
- Suggested practical setup:
  - Compose in any DAW.
  - Export the vocal melody as MIDI (or MusicXML for NEUTRINO) and sing it in OpenUtau.
  - Render to WAV and drag it into Cubase, FL or REAPER with the same BPM. Optionally try the 0.1.571+ bridge in REAPER first, the best-equipped host.
- For Miku specifically there is no free path. The cheapest legal options are the 31-day VOCALOID6/Miku V6 trials, then the US$78 Miku V6 voicebank with Editor Lite (standalone, 2 tracks) (earlier notes).

### Gaps
- No independent 2026 comparison or review of the free tools (OpenUtau/DiffSinger vs NEUTRINO vs VoiSona Chis-A) was found, so the quality ranking is an informed inference, not a measured result.
- The OpenUtau bridge and DirectML on a GTX 1650 have not been tested on the target machine.
- Effort estimates (time to a usable vocal) are not quantified in any source.
