"""Regression tests for the native synchronous get_tts.

EdgeTTSPlugin subclasses StreamingTTS, whose inherited sync adapter drove its own
event loop via ``run_until_complete`` — which raised
``RuntimeError: Cannot run the event loop while another loop is running`` when
called from inside an already-running loop (e.g. ovos-tts-server's async
handlers). The plugin now overrides get_tts to be loop-safe. These tests mock the
Edge stream so they need no network.
"""
import asyncio
import os
import tempfile
from unittest.mock import patch

from ovos_tts_plugin_edge_tts import EdgeTTSPlugin


async def _fake_stream(self, sentence, voice=None, rate=None, lang=None):
    # a couple of fake "mp3" chunks — no network
    yield b"ID3fake"
    yield b"audio-bytes"


def _plugin():
    return EdgeTTSPlugin({"voice": "en-US-AriaNeural"})


def test_get_tts_sync_context():
    p = _plugin()
    with patch.object(EdgeTTSPlugin, "stream_tts", _fake_stream), \
            tempfile.TemporaryDirectory() as d:
        out = os.path.join(d, "a.mp3")
        path, phonemes = p.get_tts("hello", out)
        assert path == out
        assert phonemes is None
        assert os.path.getsize(out) == len(b"ID3fake") + len(b"audio-bytes")


def test_get_tts_inside_running_loop():
    # the exact case that used to crash with the nested-loop RuntimeError
    p = _plugin()

    async def call():
        with patch.object(EdgeTTSPlugin, "stream_tts", _fake_stream), \
                tempfile.TemporaryDirectory() as d:
            out = os.path.join(d, "b.mp3")
            p.get_tts("hello", out)
            return os.path.getsize(out)

    n = asyncio.run(call())
    assert n > 0
