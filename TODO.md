# TODO

## Open issues
None open.

## Gaps
- [ ] No test suite (no `test/` dir, no unit tests for `stream_tts` / voice lookup).
- [ ] No coverage workflow.
- [ ] No `opm-check` workflow despite declaring an OVOS/OPM TTS plugin entry point.
- [ ] `build_tests.yml` references `neongeckocom/.github` reusable workflow; should use OpenVoiceOS/gh-automations.
- [ ] Release workflows (`publish_stable.yml`, `release_workflow.yml`) pin `TigreGotico/gh-automations` at `@master`; org standard is `@dev`.
- [ ] Committed scratch artifact: `ovos_tts_plugin_edge_tts.egg-info/` (already in `.gitignore`).
- [ ] Entry point uses legacy group `mycroft.plugin.tts` rather than `opm.plugin.tts`.

## Code TODOs
None found.
