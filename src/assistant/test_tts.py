from TTS.api import TTS

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

tts.tts_to_file(
    text="Hello Sire. Aleks voice system is ready.",
    file_path="test.wav"
)