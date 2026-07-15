
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

## Docker (ovos-tts-server)

A container image runs the plugin as an
[`ovos-tts-server`](https://github.com/OpenVoiceOS/ovos-tts-server) (ElevenLabs-compatible
API), built and pushed to GHCR by CI on every push to `dev`/`master`:

```bash
docker run -p 9666:9666 ghcr.io/openvoiceos/ovos-tts-plugin-edge-tts:latest
curl "http://localhost:9666/synthesize/hello%20world?lang=en-US" --output hello.wav
```

The served voice is baked in via the `EDGE_VOICE` build arg (default
`en-US-AriaNeural`); rebuild to change it, e.g.
`docker build --build-arg EDGE_VOICE=ar-SA-HamedNeural -t edge-tts .`. See the bundled
`docker-compose.yml`. Edge streams from Microsoft's cloud, so the container needs network access.
