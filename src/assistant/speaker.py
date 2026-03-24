import sounddevice as sd
import soundfile as sf
import time
import threading
from pathlib import Path
from piper.voice import PiperVoice
import tempfile
import wave

speaking_event = threading.Event()
last_spoken_time = 0

VOICE_PATH = str(
    Path(__file__).resolve().parent.parent.parent
    / "voices"
    / "ru_RU-dmitri-medium.onnx"
)

voice = PiperVoice.load(VOICE_PATH)


def speak(text):
    global last_spoken_time

    speaking_event.set()
    print(f"Aleks: {text}")

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:

        # create proper WAV writer
        with wave.open(f.name, "wb") as wav_file:
            voice.synthesize_wav(text, wav_file)

        audio, sample_rate = sf.read(f.name)

        sd.play(audio, sample_rate)
        sd.wait()

    last_spoken_time = time.time()
    speaking_event.clear()


def stop():
    sd.stop()
    speaking_event.clear()