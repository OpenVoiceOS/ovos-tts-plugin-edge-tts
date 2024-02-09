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
        self.voice = self.config.get("voice", "en-US-AriaNeural")
        self.rate = self.config.get("rate", "+200%")  # Default to normal speed (200%); use +0% for 100% speed
        self.output_file = self.config.get("output_file", "edge_tts_output.wav")

    async def generate_audio(self, edge_tts_communicate, file):
        async for chunk in edge_tts_communicate.stream():
            if chunk["type"] == "audio":
                file.write(chunk["data"])

        return file.name, None  # No phonemes

    def play_audio(self, wav_file):
        subprocess.run(["paplay", wav_file])

    def get_tts(self, sentence, wav_file):
        edge_tts_communicate = edge_tts.Communicate(sentence, self.voice, rate=self.rate)

        with open(wav_file, "wb") as file:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

            try:
                result = loop.run_until_complete(self.generate_audio(edge_tts_communicate, file))
                self.play_audio(result[0])
                return result
            finally:
                loop.close()

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
