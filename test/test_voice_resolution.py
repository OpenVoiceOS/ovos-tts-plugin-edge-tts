"""A per-request lang must select the voice over the configured default.

Regression: with an en-US default voice, requesting lang=ar-SA rendered Arabic
text with the English voice (self.synth injects the default voice), and edge_tts
returns NoAudioReceived on a voice/text-language mismatch. lang now wins. These
tests capture the voice handed to edge_tts, so they need no network.
"""
from unittest.mock import patch, MagicMock

from ovos_tts_plugin_edge_tts import EdgeTTSPlugin


class _FakeCommunicate:
    last_voice = None

    def __init__(self, sentence, voice, rate=None):
        _FakeCommunicate.last_voice = voice

    async def stream(self):
        yield {"type": "audio", "data": b"x"}


def _voice_for(config_voice, **get_tts_kwargs):
    p = EdgeTTSPlugin({"voice": config_voice})
    with patch("ovos_tts_plugin_edge_tts.edge_tts.Communicate", _FakeCommunicate):
        p.get_tts("مرحبا", "/tmp/_vr.mp3", **get_tts_kwargs)
    return _FakeCommunicate.last_voice


def test_lang_overrides_default_voice():
    # en-US default + lang=ar-SA -> an Arabic voice, not en-US (the old crash)
    v = _voice_for("en-US-AriaNeural", lang="ar-SA")
    assert v.startswith("ar-SA")


def test_explicit_voice_kept():
    # an explicit voice belonging to the lang is preserved
    v = _voice_for("en-US-AriaNeural", voice="ar-SA-HamedNeural", lang="ar-SA")
    assert v == "ar-SA-HamedNeural"


def test_default_voice_when_no_lang():
    v = _voice_for("en-US-AriaNeural")
    assert v == "en-US-AriaNeural"
