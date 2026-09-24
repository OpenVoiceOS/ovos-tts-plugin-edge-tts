"""A stream with no audio chunk is an error, not an empty file.

Microsoft's service refuses some clients (a GitHub runner, for one) with a
stream that carries only metadata. Some edge-tts releases end that stream
without raising, and a caller that only looks for a file then sees nothing
and no error: wakeforge's datagen counted 0 positives silently (T-2766).
These tests replace edge_tts.Communicate with a fake that streams the
metadata-only reply, so they need no network.
"""
import asyncio
import os
import tempfile
from unittest.mock import patch

import pytest

from ovos_tts_plugin_edge_tts import EdgeTTSNoAudioError, EdgeTTSPlugin


class _RefusedCommunicate:
    """What the service sends when it refuses: boundary metadata, no audio."""

    def __init__(self, *args, **kwargs):
        pass

    async def stream(self):
        yield {"type": "WordBoundary", "offset": 0, "duration": 0, "text": ""}


class _EmptyAudioCommunicate:
    """A stream whose audio chunks carry no bytes."""

    def __init__(self, *args, **kwargs):
        pass

    async def stream(self):
        yield {"type": "audio", "data": b""}


class _GoodCommunicate:
    def __init__(self, *args, **kwargs):
        pass

    async def stream(self):
        yield {"type": "WordBoundary", "offset": 0, "duration": 0, "text": "hi"}
        yield {"type": "audio", "data": b"ID3fake"}


def _plugin():
    return EdgeTTSPlugin({"voice": "en-US-AriaNeural"})


@pytest.mark.parametrize("fake", [_RefusedCommunicate, _EmptyAudioCommunicate])
def test_get_tts_raises_and_writes_no_file(fake):
    p = _plugin()
    with patch("ovos_tts_plugin_edge_tts.edge_tts.Communicate", fake), tempfile.TemporaryDirectory() as d:
        out = os.path.join(d, "a.mp3")
        with pytest.raises(EdgeTTSNoAudioError) as info:
            p.get_tts("hello", out)
        assert "en-US-AriaNeural" in str(info.value)
        assert not os.path.exists(out), "a refused request must not leave a file behind"


def test_stream_tts_raises_after_a_metadata_only_stream():
    p = _plugin()

    async def consume():
        chunks = []
        async for chunk in p.stream_tts("hello"):
            chunks.append(chunk)
        return chunks

    with patch("ovos_tts_plugin_edge_tts.edge_tts.Communicate", _RefusedCommunicate):
        with pytest.raises(EdgeTTSNoAudioError):
            asyncio.run(consume())


def test_a_stream_with_audio_is_unchanged():
    p = _plugin()
    with patch("ovos_tts_plugin_edge_tts.edge_tts.Communicate", _GoodCommunicate), tempfile.TemporaryDirectory() as d:
        out = os.path.join(d, "b.mp3")
        path, phonemes = p.get_tts("hello", out)
        assert path == out
        assert phonemes is None
        with open(out, "rb") as f:
            assert f.read() == b"ID3fake"


def test_error_is_a_runtime_error():
    # callers that catch RuntimeError for the old loop failure catch this too
    assert issubclass(EdgeTTSNoAudioError, RuntimeError)
