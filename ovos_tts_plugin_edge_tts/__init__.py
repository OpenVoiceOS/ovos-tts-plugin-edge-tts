from ovos_plugin_manager.templates.tts import StreamingTTS
import edge_tts

class EdgeTTSPlugin(StreamingTTS):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.voice = self.config.get("voice", "en-US-AriaNeural")
        self.rate = self.config.get("rate", "+0%")  # use +0% for normal speed (100%)
            
    async def stream_tts(sentence, voice=None, rate=None):
        """yield chunks of TTS audio as they become available"""
        voice = voice or self.voice
        rate = rate or self.rate
        tts = edge_tts.Communicate(sentence, voice, rate=rate)
        async for chunk in tts.stream():
            if chunk["type"] == "audio":
                yield chunk["data"]
