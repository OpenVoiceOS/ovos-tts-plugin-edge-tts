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
        self.voice = self.config.get("voice", "nl-NL-MaartenNeural")
        self.rate = self.config.get("rate", "+200%")
        self.output_file = self.config.get("output_file", "edge_tts_output.wav")

    def get_tts(self, sentence, wav_file):
        edge_tts_communicate = edge_tts.Communicate(sentence, self.voice, rate=self.rate)

        # Play audio while generating
        process = subprocess.Popen(["paplay"], stdin=subprocess.PIPE)

        with open(wav_file, "wb") as file:
            loop = asyncio.get_event_loop_policy().get_event_loop()
            async def generate_audio():
                async for chunk in edge_tts_communicate.stream():
                    if chunk["type"] == "audio":
                        file.write(chunk["data"])
                        process.stdin.write(chunk["data"])

                process.stdin.close()
                process.wait()

                return wav_file, None  # No phonemes

            loop.run_until_complete(generate_audio())

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
