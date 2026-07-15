# Microsoft Edge neural voices served through ovos-tts-server's ElevenLabs-compatible
# API. A self-contained image: any client that speaks the ovos-tts-server / ElevenLabs
# API can hit it, and it can be A/B-tested against other ovos-tts-server voices (phoonnx,
# omnivoice, ...) by pointing at a different port.
#
# Edge streams audio from Microsoft's cloud, so this container needs network access
# (it is not an offline/air-gapped voice).
FROM python:3.11-slim

# ffmpeg: edge_tts emits mp3; ovos-tts-server transcodes non-WAV plugin output to WAV.
RUN apt-get update && apt-get install -y --no-install-recommends \
        ffmpeg \
        git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

# the plugin + edge-tts + the OVOS TTS server. setuptools<81 keeps
# ovos-plugin-manager's pkg_resources usage working.
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir "setuptools<81" "." edge-tts ovos-tts-server
# TODO: drop once ovos-tts-server ships the non-WAV transcode fix (OpenVoiceOS/ovos-tts-server#137).
RUN pip install --no-cache-dir --force-reinstall --no-deps \
    "ovos-tts-server @ git+https://github.com/OpenVoiceOS/ovos-tts-server@fix/elevenlabs-nonwav-plugin-output"

# Default voice, overridable with the EDGE_VOICE build arg (any Edge voice works).
ARG EDGE_VOICE=en-US-AriaNeural
RUN useradd -m -u 1000 ovos \
    && mkdir -p /home/ovos/.config/mycroft \
    && printf '{\n  "tts": {\n    "module": "ovos-tts-plugin-edge-tts",\n    "ovos-tts-plugin-edge-tts": {\n      "voice": "%s"\n    }\n  }\n}\n' "${EDGE_VOICE}" \
        > /home/ovos/.config/mycroft/mycroft.conf \
    && chown -R 1000:1000 /home/ovos/.config
USER 1000

EXPOSE 9666
ENTRYPOINT ["ovos-tts-server", "--engine", "ovos-tts-plugin-edge-tts", \
            "--host", "0.0.0.0", "--port", "9666", "--cache"]
