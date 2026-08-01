# ovos-tts-plugin-edge-tts

A text-to-speech (TTS) plugin for [OpenVoiceOS](https://openvoiceos.org) that uses
Microsoft's [Edge TTS](https://github.com/rany2/edge-tts) engine. It streams synthesized
speech from Microsoft's cloud service, so it needs network access to work.

## Installation

```bash
pip install ovos-tts-plugin-edge-tts
```

## Configuration

Add the plugin to your user config file (`~/.config/mycroft/mycroft.conf`):

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

See the [list of voices available in Edge TTS](https://gist.github.com/BettyJJ/17cbaa1de96235a7f5773b8690a20462).

Many of the newer multilingual voices (from March 2024) also work with this plugin. For
example: `"voice": "en-US-EmmaMultilingualNeural"`.

## Docker (ovos-tts-server)

A container image runs the plugin as an
[`ovos-tts-server`](https://github.com/OpenVoiceOS/ovos-tts-server) (ElevenLabs-compatible
API). CI builds and pushes the image to GHCR on every push to `dev` or `master`.

```bash
docker run -p 9666:9666 ghcr.io/openvoiceos/ovos-tts-plugin-edge-tts:latest
curl "http://localhost:9666/synthesize/hello%20world?lang=en-US" --output hello.wav
```

The served voice is baked in through the `EDGE_VOICE` build argument (default
`en-US-AriaNeural`). Rebuild the image to change it, for example:

```bash
docker build --build-arg EDGE_VOICE=ar-SA-HamedNeural -t edge-tts .
```

See the bundled `docker-compose.yml` for a full example. Because Edge TTS streams audio
from Microsoft's cloud, the container needs network access.

## Related projects

- [OpenVoiceOS/ovos-tts-server](https://github.com/OpenVoiceOS/ovos-tts-server) — serves
  this plugin (and other OVOS TTS plugins) over an ElevenLabs-compatible HTTP API.
- [rany2/edge-tts](https://github.com/rany2/edge-tts) — the underlying Edge TTS client
  library this plugin wraps.

## License

Apache-2.0. See [LICENSE.txt](LICENSE.txt).
