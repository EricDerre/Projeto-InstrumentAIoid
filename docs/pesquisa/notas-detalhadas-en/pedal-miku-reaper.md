# "Miku" guitar pedal → free live equivalent in REAPER (research notes, 2026-10-08)

Scope: research only. Nothing was downloaded, installed or run on the user's machine.
Rig context came from the request plus `scratchpad/rig/build_rig.lua` (written in an earlier session):
- track **GUITARRA**: mono **Input 2** (UM2 INST 2), 4 channels, armed and monitored
- FX slot 1 on GUITARRA: ReaTune "Afinador" (bypassed)
- **ReaVocode "Talk Box (microfone do fone)"**: its modulator is the headset mic, sent from the "MIC TALK BOX" track (ReaStream) to GUITARRA **ch 3/4**
- "Talk Box vogais.jsfx" vowel filter
- KB-25 is MIDI device 0. The knobs send CC1–9 on ch 1 (CC2 = amp input) and the pads send CC95–112 on ch 10.

---

## 0. Bottom line

- **The pedal is almost certainly the KORG MIKU STOMP**, released in 2014 and now discontinued. It tracks the pitch of single guitar notes and feeds a Yamaha **NSX-1 "eVocaloid"** chip, which holds a licensed Miku voice. Each picked note sings the next syllable. KORG's own manual gives the latency as about 30–100 ms.
- **No free software can sing with Miku's real voice live.** Live Miku exists only in NSX-1 hardware (the Miku Stomp and Gakken's Pocket Miku). Crypton's Piapro Studio NT2, VOCALOID6, Synthesizer V, ACE Studio and Omnivocal all compose and render rather than play live.
- **Best free equivalent: REAPER's own ReaTune → Plogue Alter/Ego (free) with the free ALYS Japanese female voice.**
  - ReaTune has "Send MIDI events when pitch changes" and a "Live input" mode.
  - Alter/Ego is a real-time singing synth that sings one syllable per MIDI note from typed kana lyrics.
  - This copies the pedal's design (pitch tracking → singing chip). Only the voice is different.
  - Optional upgrade: feed that voice into the ReaVocode talk box the rig already has. The pitch then always comes from the guitar.

---

## 1. The pedal in the Short

### Identification
- **Short metadata** (YouTube oEmbed): title "The Funniest Sound Of All Time", author **Rob Chapman** (@RobChappers). Source: https://www.youtube.com/oembed?url=https://www.youtube.com/shorts/7Z4CN3d-Gts&format=json
  - I could not watch the video itself, because YouTube blocks automated page fetches.
- **Rob Chapman's full review** is "Korg Miku Pedal - the funniest pedal review ever!!" (https://www.youtube.com/watch?v=aveUEZkcQno; oEmbed confirms author Rob Chapman).
  - Laughing Squid embedded it on 16 Mar 2015 as a review of the KORG Miku Stomp: https://laughingsquid.com/?p=475783
  - A WindowsForum thread about it dates from 5 Feb 2015: https://windowsforum.com/the-water-cooler.88/korg-miku-pedal-the-funniest-pedal-review-ever.204769/
- **Equipboard** lists Rob Chapman as a Miku Stomp user and quotes the review ("the voice of Saki Fujita", "a few problems"): https://equipboard.com/items/korg-miku-stomp
- **No other Miku-voiced guitar pedal exists.** Searches for 2025/26 Miku pedals return only the Miku Stomp.
- **Conclusion:** the Short very probably shows the Miku Stomp (high confidence, but not seen directly).

### How it works (official KORG sources unless noted)
- **Monophonic.** KORG: "MIKU STOMP supports only single notes" — https://www.korg.com/us/products/effects/mikustomp/features.php
  - Gigazine: the processor analyses the guitar signal and plays Miku's voice at the detected pitch. No chords. Every pick triggers the next stored sound, so noise or a string you didn't mean to hit triggers syllables. Mute unused strings. The front pickup with the tone rolled back a little can help: https://gigazine.net/gsc_news/en/20141010-mikustomp
- **Engine:** "eVocaloid™ … based on Yamaha's next-generation NSX-1 sound engine" (KORG features page above). Korg Japan says the same: https://www.korg.com/jp/products/effects/mikustomp/features.php
- **Detection range:**
  - Spec page: E1 (41 Hz) – E6 (1,319 Hz): https://www.korg.com/us/products/effects/mikustomp/specifications.php
  - Owner's manual: E2 (82 Hz) – E6.
- **Latency:** "There is a delay of approximately 30–100 ms from when you play until MIKU STOMP produces sound" (Owner's Manual, MIKU_STOMP_JEFGSC1.pdf, 4.2 MB, 2015-06-01): https://www.korg.com/us/support/download/manual/0/375/2006/
- **Controls** (manual):
  - Effect footswitch (true bypass)
  - Effect LED (blinks in pairs when the battery is low)
  - **Selector** for what Miku sings
  - Peak LED (input too hot)
  - Mono in and mono out jacks
  - DC 9 V jack
- **Power and size** (spec page):
  - 2×AA batteries (about 5 h) or a 9 V adapter; 200 mA
  - 74×120×50 mm, 250 g
- **11 selector patterns** (manual, Effects Database https://www.effectsdatabase.com/model/korg/mikustomp, Andertons https://www.andertons.co.uk/korg/korg-miku-vocaloid-stomp-effect-unit):
  - **Random 1 / Random 2:** words picked at random from a set of 1,000 (each mode uses a different set)
  - **Scat:** random syllables such as lahh, looh and ahh
  - **Looh, Lahh, Ahh, Pahh:** a single fixed syllable each
  - **Nyan:** fixed length, and it does not follow string bends
  - **Phrase 1/2/3:** lyrics written in the Lyric Editor app
- **What it sings:**
  - A preset lyric set for the song **"Senbonzakura"**. Sources: Adorama https://www.adorama.com/komikustomp.html, AV Watch https://av.watch.impress.co.jp/docs/news/664808.html, CDM https://cdm.link/wtf-miku-stomp-box-sings-along-vocaloid-style/
  - Your own lyrics, Japanese only (romaji, hiragana or katakana), up to 6,000 characters (KORG features page).
  - The lyrics come from **"Lyrics for MIKU STOMP"**, a free KORG iPhone app (v1.2.1, Nov 2017, iOS 9.3+). You hold the iPhone over the guitar pickups to transfer them: https://apps.apple.com/bb/app/id927422952
  - The lyric feature was only offered in some countries.
  - Note: the Miku Stomp has nothing to do with "Pocket Miku" lyrics. Pocket Miku is a separate Gakken product with the same chip (see §3).
- **Release and price:** late October 2014; expected street price about ¥13,000 (AV Watch, above).
- **Discontinued:**
  - Korg Japan: "この製品の生産、販売は終了いたしました" ("production and sales of this product have ended"). https://www.korg.com/jp/products/effects/mikustomp/features.php
  - Bax-shop lists it as "Discontinued": https://www.bax-shop.co.uk/modulation/korg-miku-stomp-pedal-evocaloid-effect-pedal
  - Adorama: "no longer available".
- **Used price today:** it has become a collectible.
  - ModularGrid offers: US$654.88 (Japan, "near mint", 3 Jul 2026): https://modulargrid.net/p/offers/view/1364926
  - ModularGrid: $569.41 (UK, as new): https://modulargrid.net/p/offers/view/1306119
  - Equipboard: $650 at Gear Exchange.
  - Sweetwater's used-gear guide still shows an old $68–$100 range: https://www.sweetwater.com/used/guide/MikuStomp--korg-miku-stomp
  - In 2018 a performer reportedly paid $250 (MetaFilter comment): https://www.metafilter.com/178001/I-could-only-imagine-what-kind-of-unholy-cacophony-it-would-create

---

## 2. Free software building blocks

### 2a. Real-time audio→MIDI (pitch trackers) for REAPER / Windows 64-bit

| Tool | Format / platform | Licence / price | Mono / poly | Live? | Notes and evidence |
|---|---|---|---|---|---|
| **ReaTune (Cockos)** – already in REAPER (it is the GUITARRA "Afinador") | VST built into REAPER (x64) | Included with REAPER | Mono | **Yes** | Tuner tab has **"Send MIDI events when pitch changes"** and Buffering mode **"Live input (lowest latency possible) – low latency and high CPU usage"**. "Non-live input" adds look-ahead/delay compensation (avoid it live). https://www.cockos.com/wiki/index.php/ReaTune · The official REAPER Effects Guide says the toggle "causes a MIDI event message to be sent whenever the pitch changes", e.g. to drive a virtual instrument from a guitar played live: https://www.reaper.fm/guides/ReaEffectsGuide.pdf · Routing recipe (MIDI-only send, audio None): https://www.cockos.com/wiki/index.php/Use_Reatune_to_write_audio_to_midi · Vibrato, slides and noise create extra events: https://puremidi.com/audio-to-midi-reaper · Not in the free ReaPlugs bundle, so it can't be used in FL or Cubase (Ardour forum user, Dec 2024): https://discourse.ardour.org/t/voice-to-midi-in-ardour/111051 |
| **Dodo MIDI 2.1** (Dodo Bird Music) | VST3 Windows (.exe), VST3/AU Mac, VST3 Linux | Free (licence text not published) | Mono (no chords, per LANDR) | Yes ("imperceptible latency" claim) | v2.1 released 6 Jun 2025. Synth pitch-bend range must be 12 or 24 st, so it drives pitch with pitch-bend. Uses a master/slave instance pair (before and after the synth) with matching port numbers. Has a REAPER quick-start video. Size: v2.1 not shown; v1.6 Win64 VST was 3.7 MB (plugins4free); v1.x installer about 4.49 MB (BPB). https://dodobirdmusic.com/dodo-midi/ · https://plugins4free.com/plugin/3562 · https://bedroomproducersblog.com/2021/10/25/dodo-audio-midi-converter/ · https://blog.landr.com/audio-to-midi/ · Not documented: whether it re-sends a note-on on every pick, which matters for advancing syllables. |
| Jam Origin **MIDI Guitar 3** (beta) | Standalone + plugin, Windows 10/11 build 3.0.68 | **Not really free:** "full-featured free trial mode with occasional interruptions"; licence **USD 149.95** lifetime | Poly (MPE) | Yes | https://jam.live/downloads/ · https://jam.live/shop/ · https://jam.live/products/MG3/ (beta; "no pitch-to-MIDI system is perfect"). MG2 FAQ: an interruption dialog every 2 min unless you play the Test Piano: https://www.jamorigin.com/products/midi-guitar/ · Staff estimate of added plugin latency: "max one buffersize": https://jamosapien.com/t/new-to-jam-origin-technology-clarification-questions/4217 |
| MiGiC (Bituosity) | VST/AU 32/64-bit, 1.17 MB (2015) | Free beta, abandoned | ? | Yes (claimed) | The official site (bituosity.com) timed out today. Not recommended. https://bedroomproducersblog.com/2015/03/28/guitar-to-midi-vst/ |
| NeuralNote | VST3/AU/Standalone | Free, Apache-2.0 | Poly | **No** | README: real-time transcription isn't possible (about 120 ms CNN latency plus backward note processing). Record first, then transcribe. https://github.com/DamRsn/NeuralNote |
| **JSFX pitch→MIDI** | – | – | – | **None found** | I checked the ReaPack indexes of ReaTeam JSFX, Saike, IX, Tilr, Tukan, chokehold, Sonic Anomaly, StevieKeys, Erriez, BirdBird, Souk21, ReaTeam Scripts and MPL, plus Geraint's JSFX page. Repo list: https://reapack.com/repos. The only pitch detection is **offline**: ReaTeam script "MK Slicer" (pitch-detection mode) and MPL "PitchEditor" (YIN). Stock JSFX "tuner" detects pitch with no MIDI out, and stock "drumtrigger" makes MIDI from amplitude, not pitch: https://www.cockos.com/wiki/index.php/Jesusonic_Effects_Documentation |

Useful free MIDI clean-up JSFX for after ReaTune, from the **IX** ReaPack repo (index https://github.com/IXix/JSFX/raw/master/index.xml):
- `MIDI_KeySnap`: snap notes to the song key, hiding wrong notes
- `MIDI_SerialKiller`: pass one note at a time
- `MIDI_AntiFlam` / `MIDI_DuplicateFilter`: block double triggers
- `MIDI_Tool II`: transpose, velocity and channel

### 2b. Singing synthesizers

**Play live from MIDI (free):**

| Instrument | Format / licence | How it sings live | Free voices | Official download |
|---|---|---|---|---|
| **Plogue Alter/Ego** v1.981 (27 Jun 2025; Plogue now labels it a "legacy product") | Standalone, VST, **VST3**, AAX on Windows 10 x64 (AU is Mac only). **Free.** Needs about 100 MB disk, a dual-core CPU and 1 GB RAM. The voice data "cannot be distributed". https://plogue.com/products/alterego | "Type in your lyrics, and then play on your MIDI keyboard". It **keeps a text cursor and "advances by one syllable for each MIDI note"**. Lines are chosen with key-switch notes 0–23 or CC2 (or program change); CC3 sets the position within a line. Legato mode is mono and does not advance the syllable. Hiragana/katakana are supported (no kanji); X-SAMPA for phonemes. It is real-time and "cannot read into the future", so transitions push the vocal slightly later. User's Guide: https://s3.amazonaws.com/palterego/AlterEgo_guide.pdf | **ALYS** (VoxWave): **French + Japanese, female**, free since the Dec 2021 open-sourcing. **Bones**: English + Japanese, male, free. **Marie Ork 2**: growl/monster voice, free. Voice-bank page: https://www.plogue.com/products/voice-banks.html | Engine (Windows): https://s3.amazonaws.com/palterego/WIN_AlterEgo_v1.981.exe (via https://www.plogue.com/downloads.html#alterego; size not published). ALYS: https://labs.phundrak.com/ALYS/ALYS → `VoxWave_ALYS_for_AlterEgo_v1.101.exe`; activate by dragging the key image `VoxWave.png` onto Alter/Ego with ALYS loaded (README). The whole repo is 1.1 GiB; the installer size is not shown. Bones: https://archive.org/details/bones-v-1002 (zip **235.6 MB**, uploaded by Plogue). Marie Ork 2: https://www.karoryfer.com/karoryfer-samples/wydawnictwa/marie-ork/zip |
| AquesTone / AquesTone2 (A-Quest, Japanese) | VST 2.4, Windows XP era | Real-time singing from MIDI plus a lyrics file | – | **Not viable.** Support for both ended on 31 May 2022, and AquesTone2's free usage period expired at the end of May 2022. https://a-quest.com/products/aquestone_en.html · https://www.a-quest.com/products/aquestone2.html |

**Free Japanese / anime-style voice:**
- Live: the only free live option found is **ALYS (JP) in Alter/Ego**.
  - A soft 21-year-old female voice by French utaite Poucet, with manga-style character art. Character art licence CC BY-NC 4.0; the Alter/Ego bank is free to use: https://vocalsynth.fandom.com/wiki/ALYS
- Rendered only: **VOICEVOX** 0.25.2 is free for commercial and non-commercial use (LGPLv3).
  - Song mode since v0.16.0 (Jan 2024) with Shikoku Metan, Zundamon, Kasukabe Tsumugi, Amehare Hau and Namine Ritsu; exports WAV.
  - A credit showing VOICEVOX was used is required, and each voice library's own terms apply.
  - https://voicevox.hiroshiba.jp/ · https://voicevox.hiroshiba.jp/term/ · https://forest.watch.impress.co.jp/docs/news/1567478.html

**Can these be played live from a keyboard? No — all render first:**
- **VOCALOID6:** official FAQ: you can record MIDI in real time, but "the voice sound won't be played until Record mode is turned off. The piano sound will be played as a guide."
  - https://www.vocaloid.com/en/support/faq/613
  - VX-β is free for registered VOCALOID6 users. Its parameters change in real time during playback, but notes are entered in Cubase's Key Editor or imported: https://www.vocaloid.com/en/vocaloid6/vxbeta/
- **Hatsune Miku NT (Ver.2) / Piapro Studio NT2:** ¥19,800 (owners of older Miku products get a ¥15,400 discount price). VST3, AU and standalone; 39-day full trial. You type the melody and lyrics; no live MIDI-keyboard singing is documented.
  - https://sonicwire.com/mikunt?lang=en · https://www.famitsu.com/article/202503/36040
- **Synthesizer V Studio 2 Pro:** $99. Workflow is render vocals from a MIDI track. Dreamtonics itself says truly real-time, low-latency vocal synthesis is "theoretically impossible" because it needs look-ahead; "Live Rendering" is only background rendering.
  - https://dreamtonics.com/synthesizerv/ · https://dreamtonics.com/?p=3572
- **ACE Studio 2:** rendered in the cloud or locally ("Turbo"), with only basic real-time guide sounds. Artist $497 / Artist Pro $660 lifetime.
  - https://soundonsound.com/reviews/ace-studio-2
- **Yamaha Omnivocal (beta):** VST3 for **Cubase 15 / Nuendo 15 only**; per SOS it comes with Pro, Artist and Elements (LE/AI are not mentioned). While you play it gives "a simple synth sound for auditioning purposes"; you write lyrics in the Key Editor. Steinberg: it "relies on special, Cubase-specific integration", so it won't run in REAPER.
  - https://www.yamaha.com/en/about/business/music-connect/omnivocal/ · https://www.soundonsound.com/techniques/cubase-15-exploring-omnivocal · https://forums.steinberg.net/t/omnivocal/1013638

### 2c. Other routes and the legal picture

**Vocoder / talk box with a Miku-style vocal as modulator:**
- Free vocoders:
  - REAPER stock **ReaVocode**: 4–144 bands, https://www.cockos.com/wiki/index.php/ReaVocode. Effects Guide routing: vocal (detector) → ch 1/2, synth (carrier) → ch 3/4.
  - **Geraint Luff "Vocoder"** JSFX (FFT): https://geraintluff.github.io/jsfx/ (ReaPack index https://geraintluff.github.io/jsfx/index.xml)
  - **Tukan "Vocoder S2"** JSFX (ReaPack index https://github.com/TukanStudios/TUKAN_STUDIOS_PLUGINS/raw/main/index2.xml)
  - TAL-Vocoder 3 is now a demo that makes "a rising white noise sound every minute": https://tal-software.com/products/tal-vocoder
- With the guitar as carrier, the output keeps the guitar's pitch: chords work and there are no tracking errors. The vocal only supplies vowels and consonants.
- Modulator choices:
  - (a) Alter/Ego driven by ReaTune (hybrid, see §3 #2)
  - (b) a pre-rendered phrase loop from VOICEVOX Song, Alter/Ego, or legally licensed Miku NT renders
- **Formant / vowel filter:** the rig's "Talk Box vogais.jsfx" can be animated, e.g. with REAPER parameter modulation. This gives vowels only, not Miku.
- **Sampled "Miku-like" instruments:**
  - No free, licensed Miku sample instrument (SFZ, SF2 or Kontakt) was found.
  - Official commercial example: Sonicwire's "Hatsune Miku Glitch Vocal Tool" (about 80 Miku V3 samples, £19.95, requires Ableton Live 9.1.6 Suite + Max for Live): https://rekkerd.org/?p=91405
  - Fan SoundFonts exist, e.g. Polyphone's "Cutie Mew Mew Magic – Hatsune Miku", a vocal "isolated out from Fox's track" with no Crypton permission stated: https://www.polyphone.io/en/soundfonts/vocals/2061-cutie-mew-mew-magic-hatsune-miku. **Avoid these.**
- **Crypton licensing:**
  - Character illustrations are CC BY-NC 3.0 plus the PCL. For vocals made with Crypton software, see each product's EULA: https://piapro.net/intl/en_for_creators.html
  - Miku V3 EULA: synthesized singing may be used commercially or non-commercially (some uses need prior contact), but not "as a component of any competing software product". The software and library may not be reproduced or redistributed. https://ec.crypton.co.jp/download/pdf/eula_mikuv3e.pdf
  - Hatsune Miku NT EULA:
    - The licence is for **non-commercial use**; commercial use needs prior contact and possibly a fee.
    - It bars redistributing the product, including "formats converted for other products".
    - It bars using it as a component of other software.
    - It bars creating unrelated virtual singers.
    - https://ec.crypton.co.jp/download/pdf/eula_virtualsinger.pdf
  - Practical reading: private renders from your own licence used live are fine. Ripped or "fan" Miku sample instruments, or redistributing a self-made one, are not.

### 2d. Fan-made "Miku Stomp" emulations
- **None found** (JSFX, VST, Max for Live or Pure Data). I searched the ReaPack indexes listed above, GitHub and web results, maxforlive results, and Pd/Pocket Miku/eVY1 queries.
- The only Miku Max for Live product is the commercial glitch tool above, which is not a guitar emulation.
- The working DIY recipe is pitch-to-MIDI → a singing synth or NSX-1 hardware, which is what §3 builds.

---

## 3. Ranked recommendation for a live rig in REAPER 7.6x

### #1 (free, closest to the pedal): ReaTune → Alter/Ego + ALYS JP

**Install**
1. Install Alter/Ego (VST3 x64), then ALYS (`VoxWave_ALYS_for_AlterEgo_v1.101.exe`).
2. Open Alter/Ego, load ALYS (Japanese), and drag `VoxWave.png` onto it to activate.
3. In REAPER: Options › Preferences › Plug-ins › VST › Re-scan.
4. Optional: install ReaPack and import the IX repo for the MIDI clean-up JSFX.

**Wiring (keeps the existing GUITARRA chain untouched)**
1. **New track "MIKU TRACKER"**:
   - Input: Mono → **Input 2** (the same UM2 INST input as GUITARRA). Arm it, set monitoring **On**, and in the arm button's right-click menu choose **Record: disable (input monitoring only)**.
   - Routing: **untick Master/parent send**, so the clean DI is never heard.
   - FX chain:
     1. ReaGate (just above string noise)
     2. Optional ReaEQ HPF about 70 Hz / LPF about 3–4 kHz
     3. **ReaTune** → Tuner tab → Buffering mode **Live input**, tick **Send MIDI events when pitch changes**. Start with a small Window size and raise it (or raise Overlap) if low notes jump octaves.
     4. Optional IX `MIDI_KeySnap` (song key), `MIDI_SerialKiller`, `MIDI_AntiFlam`; `MIDI_Tool II` +12 st if the voice sounds too low
2. **New track "MIKU"**: insert **Alter/Ego (VST3i)** with ALYS JP.
   - Words tab: one line per "pattern", e.g. line 0 `ら ら ら …`, line 1 `にゃん にゃん …`, line 2 = your own kana lyrics.
   - Keep **Legato off**, so every note advances a syllable.
   - After it: your pitch shifter/formant for brightness, then reverb/delay.
3. **Send MIKU TRACKER → MIKU:** Audio **None**, MIDI **All → All** (the ReaTune wiki recipe). The MIKU track does not need to be armed to play from the send.
4. **Selector-knob emulation (optional):**
   - Also arm MIKU with input MIDI: KB-25 and monitoring On.
   - Put the existing "Filtro MIDI.jsfx" first, because KB-25 knob CC2 is also Alter/Ego's line-select.
   - Switch lines with key-switch notes 0–23 (needs octave-down) or CC2.
   - Or just play Miku from the KB-25 when tracking isn't needed.
5. **Dry vs. Miku:**
   - Balance the GUITARRA and MIKU faders.
   - For "Miku only", mute GUITARRA; MIDI-learn "Track: Toggle mute" to a KB-25 control.
   - For "guitar only", mute MIKU or bypass ReaTune.

**Expected latency (estimate, not measured):**
- ASIO 48 samples @ 48 kHz = 1 ms per buffer (about 2 ms plus driver overhead).
- ReaTune needs roughly two cycles of the fundamental: low E2 ≈ 24 ms, A3 ≈ 9 ms, plus the window → about 10–45 ms.
- Alter/Ego consonant onset, with no look-ahead → about 10–40 ms.
- **Total ≈ 25–90 ms**, in the same range as the pedal's 30–100 ms.

**Limitations:**
- Single notes only.
- Octave and wrong-note glitches, especially on low strings. Play above the 5th fret or on the higher strings, use the neck pickup and mute other strings — the same tips KORG gives.
- **Re-picking the same pitch may not trigger a new note**, because ReaTune sends events "when pitch changes". The pedal does advance on every pick, so test this.
- Bends and vibrato can add notes.
- CPU: ReaTune "Live input" uses a lot of CPU (Cockos wiki); Alter/Ego is light.
- ALYS is not Miku's voice.

### #2 (free, most musical): the same voice used as the talk-box modulator
- Send the MIKU track's audio to **GUITARRA ch 3/4**, exactly like the MIC TALK BOX send.
- Mute or stop the headset-mic track, untick MIKU's master send, and switch on the ReaVocode "Talk Box" pad (CC 102).
- The guitar (after the amp sims) is the carrier. The pitch is always the guitar's, chords work, and wrong tracker notes only change the vowel/consonant colour.
- Syllables still lag the pick by the tracker and synth delay.

### #3 (free, zero tracking): phrase-loop talk box
- Render a short Japanese "la-la / nyan" phrase (VOICEVOX Song with credit, or Alter/Ego/ALYS).
- Put it on a track looped to the song tempo and send it to GUITARRA ch 3/4.
- This works for chords and riffs; the words follow the loop, not your picking.

### Paid upgrades (brief)
- **Jam Origin MIDI Guitar 3**: USD 149.95 lifetime licence. Replaces ReaTune with better polyphonic/MPE tracking. The trial has interruptions.
- **Gakken Pocket Miku (NSX-39)**: the same NSX-1 chip as the Stomp, with the real licensed Miku eVocaloid. Discontinued (¥4,980 + tax at launch; Adafruit $59.95, no longer stocked); buy used.
  - It talks MIDI over USB: on ch 1 every Note On sings the next character of the current lyric, and lyrics are loaded by SysEx or Gakken's web app.
  - REAPER wiring: MIKU TRACKER → **MIDI Hardware Output: NSX-39**; its headphone out → UM2 Input 1 → a monitored track.
  - https://otonanokagaku.net/nsx39/ · https://otonanokagaku.net/nsx39/data/nsx39midiguide.pdf · https://adafruit.com/product/2332
- **Dreamtonics Vocoflex**: $199. Real-time voice morphing, 35 ms (lowest-latency mode) to 105 ms round trip. Built for solo vocals (no distortion on the input); SOS got "an interesting vocal character" from eBow guitar, with octave-jump problems. Not lyric-based.
  - https://dreamtonics.com/vocoflex/ · https://www.soundonsound.com/reviews/dreamtonics-vocoflex
- **Used KORG Miku Stomp**: about $570–655 in 2026 listings (see §1).
- **Hatsune Miku NT2**: ¥19,800, render-only. Only useful for legal pre-rendered Miku phrases, and its EULA restricts commercial use.

---

## 4. Gaps / not verifiable this session
- I could not watch the Short; the identification rests on metadata plus Rob Chapman's 2015 review.
- Cockos forum threads (plug-in authors' posts) are behind a bot check and could not be read.
- Installer sizes for Alter/Ego, ALYS, MIDI Guitar 3 and Dodo 2.1 are not published, and HEAD requests were blocked by the proxy.
- ReaTune's exact latency and its behaviour on repeated identical notes, and Dodo MIDI's note-on vs pitch-bend behaviour, are undocumented. Test before a gig.
- My web-fetch quota ran out at the end of the session, so OpenUtau/UTAU details were not checked (they are render-only editors in any case).
