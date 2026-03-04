import whisper
import sounddevice as sd
import numpy as np

model = whisper.load_model("base")

SAMPLE_RATE = 16000
DURATION = 5  # seconds

def listen() -> str:
    print("Listening...")

    audio = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype="float32")
    sd.wait()

    audio = audio.flatten()
    result = model.transcribe(audio, fp16=False)

    text = result["text"].strip()
    print("Heard:", text)
    return text