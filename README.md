
TTS plugin for [OVOS](https://openvoiceos.org) based on [Edge-TTS](https://github.com/rany2/edge-tts)

## Configuration
Configuration parameters to add in the user config: `~/.config/mycroft/mycroft.conf`

```javascript
"tts": {
    "module": "ovos-tts-plugin-edge-tts",
    "ovos-tts-plugin-edge-tts": {
        "voice": "en-US-AriaNeural", 
        // =100% speed; use "+50%" for 150%, or "+100%" for 200% speech rate etc for adjusting speed
        "rate": "+0%" 
    }
}
```
See for voices: [list of voices available in Edge TTS](https://gist.github.com/BettyJJ/17cbaa1de96235a7f5773b8690a20462). 

Also a lot of the latest generation [multilingual voices](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts#multilingual-voices) (from March 2024) work with this plug-in. For instance: `"voice": "en-US-EmmaMultilingualNeural"`.

##### Installation

`pip install ovos-tts-plugin-edge-tts`
