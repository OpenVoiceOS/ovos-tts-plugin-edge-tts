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
        self.rate = self.config.get("rate", "+150%")  # use +0% for normal speed (100%)
        self.output_file = self.config.get("output_file", "edge_tts_output.wav")
        self.played_chunks = set()  # Set to track played chunks

    async def generate_audio(self, edge_tts_communicate, file):
        process = subprocess.Popen(["paplay"], stdin=subprocess.PIPE)

        try:
            async for chunk in edge_tts_communicate.stream():
                if chunk["type"] == "audio":
                    file.write(chunk["data"])
                    index = chunk.get("index")  # Use get() to handle missing key gracefully
                    if index is not None and index not in self.played_chunks:
                        self.played_chunks.add(index)
                        asyncio.create_task(self.play_audio(file.name, process.stdin, chunk["data"]))

        finally:
            process.stdin.close()
            process.wait()

        return file.name, None  # No phonemes

    async def play_audio(self, wav_file, stdin, data):
        stdin.write(data)
        await asyncio.sleep(0.1)  # Add a small delay to ensure proper playback
        stdin.flush()

    def get_tts(self, sentence, wav_file):
        edge_tts_communicate = edge_tts.Communicate(sentence, self.voice, rate=self.rate)

        with open(wav_file, "wb") as file:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

            try:
                result = loop.run_until_complete(self.generate_audio(edge_tts_communicate, file))
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
