import edge_tts
from ovos_plugin_manager.templates.tts import StreamingTTS
from ovos_utils.lang import standardize_lang_tag


VOICES = {'af-ZA': ['af-ZA-AdriNeural', 'af-ZA-WillemNeural'],
         'am-ET': ['am-ET-AmehaNeural', 'am-ET-MekdesNeural'],
         'ar-AE': ['ar-AE-FatimaNeural', 'ar-AE-HamdanNeural'],
         'ar-BH': ['ar-BH-AliNeural', 'ar-BH-LailaNeural'],
         'ar-DZ': ['ar-DZ-AminaNeural', 'ar-DZ-IsmaelNeural'],
         'ar-EG': ['ar-EG-SalmaNeural', 'ar-EG-ShakirNeural'],
         'ar-IQ': ['ar-IQ-BasselNeural', 'ar-IQ-RanaNeural'],
         'ar-JO': ['ar-JO-SanaNeural', 'ar-JO-TaimNeural'],
         'ar-KW': ['ar-KW-FahedNeural', 'ar-KW-NouraNeural'],
         'ar-LB': ['ar-LB-LaylaNeural', 'ar-LB-RamiNeural'],
         'ar-LY': ['ar-LY-ImanNeural', 'ar-LY-OmarNeural'],
         'ar-MA': ['ar-MA-JamalNeural', 'ar-MA-MounaNeural'],
         'ar-OM': ['ar-OM-AbdullahNeural', 'ar-OM-AyshaNeural'],
         'ar-QA': ['ar-QA-AmalNeural', 'ar-QA-MoazNeural'],
         'ar-SA': ['ar-SA-HamedNeural', 'ar-SA-ZariyahNeural'],
         'ar-SY': ['ar-SY-AmanyNeural', 'ar-SY-LaithNeural'],
         'ar-TN': ['ar-TN-HediNeural', 'ar-TN-ReemNeural'],
         'ar-YE': ['ar-YE-MaryamNeural', 'ar-YE-SalehNeural'],
         'az-AZ': ['az-AZ-BabekNeural', 'az-AZ-BanuNeural'],
         'bg-BG': ['bg-BG-BorislavNeural', 'bg-BG-KalinaNeural'],
         'bn-BD': ['bn-BD-NabanitaNeural', 'bn-BD-PradeepNeural'],
         'bn-IN': ['bn-IN-BashkarNeural', 'bn-IN-TanishaaNeural'],
         'bs-BA': ['bs-BA-GoranNeural', 'bs-BA-VesnaNeural'],
         'ca-ES': ['ca-ES-EnricNeural', 'ca-ES-JoanaNeural'],
         'cs-CZ': ['cs-CZ-AntoninNeural', 'cs-CZ-VlastaNeural'],
         'cy-GB': ['cy-GB-AledNeural', 'cy-GB-NiaNeural'],
         'da-DK': ['da-DK-ChristelNeural', 'da-DK-JeppeNeural'],
         'de-AT': ['de-AT-IngridNeural', 'de-AT-JonasNeural'],
         'de-CH': ['de-CH-JanNeural', 'de-CH-LeniNeural'],
         'de-DE': ['de-DE-AmalaNeural',
                   'de-DE-ConradNeural',
                   'de-DE-KatjaNeural',
                   'de-DE-KillianNeural'],
         'el-GR': ['el-GR-AthinaNeural', 'el-GR-NestorasNeural'],
         'en-AU': ['en-AU-NatashaNeural', 'en-AU-WilliamNeural'],
         'en-CA': ['en-CA-ClaraNeural', 'en-CA-LiamNeural'],
         'en-GB': ['en-GB-LibbyNeural',
                   'en-GB-MaisieNeural',
                   'en-GB-RyanNeural',
                   'en-GB-SoniaNeural',
                   'en-GB-ThomasNeural'],
         'en-HK': ['en-HK-SamNeural', 'en-HK-YanNeural'],
         'en-IE': ['en-IE-ConnorNeural', 'en-IE-EmilyNeural'],
         'en-IN': ['en-IN-NeerjaNeural', 'en-IN-PrabhatNeural'],
         'en-KE': ['en-KE-AsiliaNeural', 'en-KE-ChilembaNeural'],
         'en-NG': ['en-NG-AbeoNeural', 'en-NG-EzinneNeural'],
         'en-NZ': ['en-NZ-MitchellNeural', 'en-NZ-MollyNeural'],
         'en-PH': ['en-PH-JamesNeural', 'en-PH-RosaNeural'],
         'en-SG': ['en-SG-LunaNeural', 'en-SG-WayneNeural'],
         'en-TZ': ['en-TZ-ElimuNeural', 'en-TZ-ImaniNeural'],
         'en-US': ['en-US-AriaNeural',
                   'en-US-AnaNeural',
                   'en-US-ChristopherNeural',
                   'en-US-EricNeural',
                   'en-US-GuyNeural',
                   'en-US-JennyNeural',
                   'en-US-MichelleNeural',
                   'en-US-RogerNeural',
                   'en-US-SteffanNeural'],
         'en-ZA': ['en-ZA-LeahNeural', 'en-ZA-LukeNeural'],
         'es-AR': ['es-AR-ElenaNeural', 'es-AR-TomasNeural'],
         'es-BO': ['es-BO-MarceloNeural', 'es-BO-SofiaNeural'],
         'es-CL': ['es-CL-CatalinaNeural', 'es-CL-LorenzoNeural'],
         'es-CO': ['es-CO-GonzaloNeural', 'es-CO-SalomeNeural'],
         'es-CR': ['es-CR-JuanNeural', 'es-CR-MariaNeural'],
         'es-CU': ['es-CU-BelkysNeural', 'es-CU-ManuelNeural'],
         'es-DO': ['es-DO-EmilioNeural', 'es-DO-RamonaNeural'],
         'es-EC': ['es-EC-AndreaNeural', 'es-EC-LuisNeural'],
         'es-ES': ['es-ES-AlvaroNeural', 'es-ES-ElviraNeural', 'es-ES-ManuelEsCUNeural'],
         'es-GQ': ['es-GQ-JavierNeural', 'es-GQ-TeresaNeural'],
         'es-GT': ['es-GT-AndresNeural', 'es-GT-MartaNeural'],
         'es-HN': ['es-HN-CarlosNeural', 'es-HN-KarlaNeural'],
         'es-MX': ['es-MX-DaliaNeural', 'es-MX-JorgeNeural', 'es-MX-LorenzoEsCLNeural'],
         'es-NI': ['es-NI-FedericoNeural', 'es-NI-YolandaNeural'],
         'es-PA': ['es-PA-MargaritaNeural', 'es-PA-RobertoNeural'],
         'es-PE': ['es-PE-AlexNeural', 'es-PE-CamilaNeural'],
         'es-PR': ['es-PR-KarinaNeural', 'es-PR-VictorNeural'],
         'es-PY': ['es-PY-MarioNeural', 'es-PY-TaniaNeural'],
         'es-SV': ['es-SV-LorenaNeural', 'es-SV-RodrigoNeural'],
         'es-US': ['es-US-AlonsoNeural', 'es-US-PalomaNeural'],
         'es-UY': ['es-UY-MateoNeural', 'es-UY-ValentinaNeural'],
         'es-VE': ['es-VE-PaolaNeural', 'es-VE-SebastianNeural'],
         'et-EE': ['et-EE-AnuNeural', 'et-EE-KertNeural'],
         'fa-IR': ['fa-IR-DilaraNeural', 'fa-IR-FaridNeural'],
         'fi-FI': ['fi-FI-HarriNeural', 'fi-FI-NooraNeural'],
         'fil-PH': ['fil-PH-AngeloNeural', 'fil-PH-BlessicaNeural'],
         'fr-BE': ['fr-BE-CharlineNeural', 'fr-BE-GerardNeural'],
         'fr-CA': ['fr-CA-AntoineNeural', 'fr-CA-JeanNeural', 'fr-CA-SylvieNeural'],
         'fr-CH': ['fr-CH-ArianeNeural', 'fr-CH-FabriceNeural'],
         'fr-FR': ['fr-FR-DeniseNeural', 'fr-FR-EloiseNeural', 'fr-FR-HenriNeural'],
         'ga-IE': ['ga-IE-ColmNeural', 'ga-IE-OrlaNeural'],
         'gl-ES': ['gl-ES-RoiNeural', 'gl-ES-SabelaNeural'],
         'gu-IN': ['gu-IN-DhwaniNeural', 'gu-IN-NiranjanNeural'],
         'he-IL': ['he-IL-AvriNeural', 'he-IL-HilaNeural'],
         'hi-IN': ['hi-IN-MadhurNeural', 'hi-IN-SwaraNeural'],
         'hr-HR': ['hr-HR-GabrijelaNeural', 'hr-HR-SreckoNeural'],
         'hu-HU': ['hu-HU-NoemiNeural', 'hu-HU-TamasNeural'],
         'id-ID': ['id-ID-ArdiNeural', 'id-ID-GadisNeural'],
         'is-IS': ['is-IS-GudrunNeural', 'is-IS-GunnarNeural'],
         'it-IT': ['it-IT-DiegoNeural', 'it-IT-ElsaNeural', 'it-IT-IsabellaNeural'],
         'ja-JP': ['ja-JP-KeitaNeural', 'ja-JP-NanamiNeural'],
         'jv-ID': ['jv-ID-DimasNeural', 'jv-ID-SitiNeural'],
         'ka-GE': ['ka-GE-EkaNeural', 'ka-GE-GiorgiNeural'],
         'kk-KZ': ['kk-KZ-AigulNeural', 'kk-KZ-DauletNeural'],
         'km-KH': ['km-KH-PisethNeural', 'km-KH-SreymomNeural'],
         'kn-IN': ['kn-IN-GaganNeural', 'kn-IN-SapnaNeural'],
         'ko-KR': ['ko-KR-InJoonNeural', 'ko-KR-SunHiNeural'],
         'lo-LA': ['lo-LA-ChanthavongNeural', 'lo-LA-KeomanyNeural'],
         'lt-LT': ['lt-LT-LeonasNeural', 'lt-LT-OnaNeural'],
         'lv-LV': ['lv-LV-EveritaNeural', 'lv-LV-NilsNeural'],
         'mk-MK': ['mk-MK-AleksandarNeural', 'mk-MK-MarijaNeural'],
         'ml-IN': ['ml-IN-MidhunNeural', 'ml-IN-SobhanaNeural'],
         'mn-MN': ['mn-MN-BataaNeural', 'mn-MN-YesuiNeural'],
         'mr-IN': ['mr-IN-AarohiNeural', 'mr-IN-ManoharNeural'],
         'ms-MY': ['ms-MY-OsmanNeural', 'ms-MY-YasminNeural'],
         'mt-MT': ['mt-MT-GraceNeural', 'mt-MT-JosephNeural'],
         'my-MM': ['my-MM-NilarNeural', 'my-MM-ThihaNeural'],
         'nb-NO': ['nb-NO-FinnNeural', 'nb-NO-PernilleNeural'],
         'ne-NP': ['ne-NP-HemkalaNeural', 'ne-NP-SagarNeural'],
         'nl-BE': ['nl-BE-ArnaudNeural', 'nl-BE-DenaNeural'],
         'nl-NL': ['nl-NL-ColetteNeural', 'nl-NL-FennaNeural', 'nl-NL-MaartenNeural'],
         'pl-PL': ['pl-PL-MarekNeural', 'pl-PL-ZofiaNeural'],
         'ps-AF': ['ps-AF-GulNawazNeural', 'ps-AF-LatifaNeural'],
         'pt-BR': ['pt-BR-AntonioNeural', 'pt-BR-FranciscaNeural'],
         'pt-PT': ['pt-PT-DuarteNeural', 'pt-PT-RaquelNeural'],
         'ro-RO': ['ro-RO-AlinaNeural', 'ro-RO-EmilNeural'],
         'ru-RU': ['ru-RU-DmitryNeural', 'ru-RU-SvetlanaNeural'],
         'si-LK': ['si-LK-SameeraNeural', 'si-LK-ThiliniNeural'],
         'sk-SK': ['sk-SK-LukasNeural', 'sk-SK-ViktoriaNeural'],
         'sl-SI': ['sl-SI-PetraNeural', 'sl-SI-RokNeural'],
         'so-SO': ['so-SO-MuuseNeural', 'so-SO-UbaxNeural'],
         'sq-AL': ['sq-AL-AnilaNeural', 'sq-AL-IlirNeural'],
         'sr-RS': ['sr-RS-NicholasNeural', 'sr-RS-SophieNeural'],
         'su-ID': ['su-ID-JajangNeural', 'su-ID-TutiNeural'],
         'sv-SE': ['sv-SE-MattiasNeural', 'sv-SE-SofieNeural'],
         'sw-KE': ['sw-KE-RafikiNeural', 'sw-KE-ZuriNeural'],
         'sw-TZ': ['sw-TZ-DaudiNeural', 'sw-TZ-RehemaNeural'],
         'ta-IN': ['ta-IN-PallaviNeural', 'ta-IN-ValluvarNeural'],
         'ta-LK': ['ta-LK-KumarNeural', 'ta-LK-SaranyaNeural'],
         'ta-MY': ['ta-MY-KaniNeural', 'ta-MY-SuryaNeural'],
         'ta-SG': ['ta-SG-AnbuNeural', 'ta-SG-VenbaNeural'],
         'te-IN': ['te-IN-MohanNeural', 'te-IN-ShrutiNeural'],
         'th-TH': ['th-TH-NiwatNeural', 'th-TH-PremwadeeNeural'],
         'tr-TR': ['tr-TR-AhmetNeural', 'tr-TR-EmelNeural'],
         'uk-UA': ['uk-UA-OstapNeural', 'uk-UA-PolinaNeural'],
         'ur-IN': ['ur-IN-GulNeural', 'ur-IN-SalmanNeural'],
         'ur-PK': ['ur-PK-AsadNeural', 'ur-PK-UzmaNeural'],
         'uz-UZ': ['uz-UZ-MadinaNeural', 'uz-UZ-SardorNeural'],
         'vi-VN': ['vi-VN-HoaiMyNeural', 'vi-VN-NamMinhNeural'],
         'zh-CN': ['zh-CN-XiaoxiaoNeural',
                   'zh-CN-XiaoyiNeural',
                   'zh-CN-YunjianNeural',
                   'zh-CN-YunxiNeural',
                   'zh-CN-YunxiaNeural',
                   'zh-CN-YunyangNeural'],
         'zh-CN-liaoning': ['zh-CN-liaoning-XiaobeiNeural'],
         'zh-CN-shaanxi': ['zh-CN-shaanxi-XiaoniNeural'],
         'zh-HK': ['zh-HK-HiuGaaiNeural', 'zh-HK-HiuMaanNeural', 'zh-HK-WanLungNeural'],
         'zh-TW': ['zh-TW-HsiaoChenNeural',
                   'zh-TW-YunJheNeural',
                   'zh-TW-HsiaoYuNeural'],
         'zu-ZA': ['zu-ZA-ThandoNeural', 'zu-ZA-ThembaNeural']
}


class EdgeTTSPlugin(StreamingTTS):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, audio_ext="mp3")
        self.voice = self.config.get("voice", "en-US-AriaNeural")
        self.rate = self.config.get("rate", "+0%")  # use +0% for normal speed (100%)

    def available_languages(self) -> set:
        return set([standardize_lang_tag(l)
                    for l in VOICES.keys()])

    async def stream_tts(self, sentence, voice=None, rate=None, lang=None):
        """yield chunks of TTS audio as they become available"""
        if lang and not voice:
            lang = standardize_lang_tag(lang, macro=True)
            if lang in VOICES:
                voice = VOICES[lang][0]
        voice = voice or self.voice
        rate = rate or self.rate
        tts = edge_tts.Communicate(sentence, voice, rate=rate)
        async for chunk in tts.stream():
            if chunk["type"] == "audio":
                yield chunk["data"]


if __name__ == "__main__":
    t = EdgeTTSPlugin({})
    t.get_tts("hello world", "test.wav",
              lang="en-us",
              voice="en-US-AriaNeural")