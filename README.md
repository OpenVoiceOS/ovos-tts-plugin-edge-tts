### ovos-tts-plugin-edge-tts

TTS plugin for [OVOS](https://openvoiceos.org) based on [Edge-TTS](https://github.com/rany2/edge-tts)

Configuration parameters to add in the user config: `~/.config/mycroft/mycroft.conf`

```json
"tts": {
    "module": "ovos-tts-plugin-edge-tts",
    "ovos-tts-plugin-edge-tts": {
        "voice": "en-US-AriaNeural", //Choose the voice name and lang-code (see list below)
        "rate": "+0%" //=100% speed; use "+150%" or "+200%" etc for adjusting speed
    }
}
```
See for voices: [list of voices available in Edge TTS](https://gist.github.com/BettyJJ/17cbaa1de96235a7f5773b8690a20462). 


##### Installation

`pip install git+https://github.com/OpenVoiceOS/ovos-tts-plugin-edge-tts`
