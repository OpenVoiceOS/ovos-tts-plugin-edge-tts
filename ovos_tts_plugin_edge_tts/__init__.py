from ovos_plugin_manager.templates.tts import StreamingTTS
import edge_tts

class EdgeTTSPlugin(StreamingTTS):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.voice = self.config.get("voice", "en-US-AriaNeural")
        self.rate = self.config.get("rate", "+0%")  # use +0% for normal speed (100%)
            
    async def stream_audio(sentence):
        """yield chunks of TTS audio as they become available"""
        tts = edge_tts.Communicate(sentence, self.voice, rate=self.rate)
        async for chunk in tts.stream():
            if chunk["type"] == "audio":
                yield chunk["data"]
