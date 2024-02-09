from ovos_plugin_manager.templates.tts import TTS, TTSValidator
from ovos_utils.log import LOG
import asyncio
import subprocess
import edge_tts

class EdgeTTSPlugin(TTS):
    def __init__(self, lang, config):
        super(EdgeTTSPlugin, self).__init__(lang, config,
                                            EdgeTTSValidator(self), 'wav')
        self.config = config.get("ovos-tts-plugin-edge-tts", {})
        self.play_streaming = self.config.get("play_streaming", False)
        self.voice = self.config.get("voice", "en-US-AriaNeural")
        self.rate = self.config.get("rate", "+150%")  # use +0% for normal speed (100%)

    async def stream_audio(sentence):
        """yield chunks of TTS audio as they become available"""
        tts = edge_tts.Communicate(sentence, self.voice, rate=self.rate)
        async for chunk in tts.stream():
            if chunk["type"] == "audio":
                yield chunk["data"]
            
    async def generate_audio(self, sentence, wav_file):
        """save streamed TTS to wav file, if configured also play TTS as it becomes available"""
        if self.play_streaming:
            process = subprocess.Popen(["paplay"], stdin=subprocess.PIPE)
        else:
            process = None

        with open(wav_file, "wb") as f:
            try:
                async for chunk in self.stream_audio(sentence):
                    if process:
                        process.stdin.write(data)
                        process.stdin.flush()
                    f.write(chunk)
            finally:
                if process:
                    process.stdin.close()
                    process.wait()
        return wav_file

    def get_tts(self, sentence, wav_file):
        """wrap streaming TTS into sync usage"""
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            wav_file = loop.run_until_complete(self.generate_audio(sentence, wav_file))
        finally:
            loop.close()
        return wav_file, None  # No phonemes

class EdgeTTSValidator(TTSValidator):
    def __init__(self, tts):
        super(EdgeTTSValidator, self).__init__(tts)

    def validate_lang(self):
        pass

    def validate_connection(self):
        # EdgeTTS is local, so no need for connection validation
        pass

    def get_tts_class(self):
        return EdgeTTSPlugin
