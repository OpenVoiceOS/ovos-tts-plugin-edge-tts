# ovos-tts-plugin-edge-tts

OpenVoiceOS streaming TTS plugin wrapping Microsoft Edge TTS (the `edge-tts` library, Azure neural voices over the public Edge endpoint, no API key).

## Setup
```bash
pip install .            # from source
# or
pip install ovos-tts-plugin-edge-tts
```
Runtime deps: `ovos-plugin-manager>=1.0.0,<3.0.0`, `edge-tts>=6.1.9`.

## Test
No test suite exists. Manual smoke test:
```bash
python ovos_tts_plugin_edge_tts/__init__.py   # synthesizes "hello world" to test.wav
```

## Lint/Typecheck
None configured.

## Layout
- `ovos_tts_plugin_edge_tts/__init__.py` — the whole plugin: `EdgeTTSPlugin(StreamingTTS)` plus a large `VOICES` dict mapping BCP-47 lang tags to Edge voice IDs. `stream_tts()` is async and yields mp3 audio chunks via `edge_tts.Communicate(...).stream()`.
- `ovos_tts_plugin_edge_tts/version.py` — semver block.
- `setup.py` — packaging; entry point declared under group **`mycroft.plugin.tts`** as `ovos-tts-plugin-edge-tts = ovos_tts_plugin_edge_tts:EdgeTTSPlugin`.

Config keys: `voice` (default `en-US-AriaNeural`), `rate` (default `+0%`, e.g. `+50%` for 150% speed).

## Conventions (Org hard rules)
- Branches: work on `dev`, release via `master`. NEVER `main`.
- NEVER edit `version.py`; gh-automations bumps semver from conventional-commit prefixes (`feat:`, `fix:`, `feat!:`).
- New repos private by default.
- Commit identity: `JarbasAi <jarbasai@mailfence.com>`.
- Reference `OpenVoiceOS/gh-automations` reusable workflows at `@dev`.
- No Neon / `neon-*` references.
- No meta-commentary (no history, no dates) in docs, commits, code comments.
- CI is provided by OpenVoiceOS/gh-automations reusable workflows.

## Gotchas
- Entry point uses the legacy `mycroft.plugin.tts` group, not `opm.plugin.tts`.
- Synthesis hits the live Edge endpoint over the network; no offline mode and no API key.
- `available_languages` is derived from `VOICES.keys()`; multilingual voices (e.g. `en-US-EmmaMultilingualNeural`) work but are not listed in the dict.
- `*.egg-info/` is committed despite being in `.gitignore`.
- Release workflows pin `TigreGotico/gh-automations` at `@master`; org standard is `@dev`. The build_tests workflow still references `neongeckocom/.github`.
