import subprocess
import tempfile
import time
import threading
import wave
from pathlib import Path
from piper.voice import PiperVoice

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

        with wave.open(f.name, "wb") as wav_file:
            voice.synthesize_wav(text, wav_file)

        subprocess.run(
            ["aplay", "-q", f.name],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

    last_spoken_time = time.time()
    speaking_event.clear()


def stop():
    speaking_event.clear()