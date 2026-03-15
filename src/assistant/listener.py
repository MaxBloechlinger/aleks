import sounddevice as sd
import numpy as np
import whisper
import tempfile
import wave
import time

from assistant.speaker import speaking

model = whisper.load_model("base")


def listen():

    # wait while Aleks is speaking
    while speaking:
        time.sleep(0.1)

    print("Listening...")

    samplerate = 16000
    duration = 5

    recording = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        with wave.open(f.name, "wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(samplerate)
            wf.writeframes(recording.tobytes())

        audio_path = f.name

    result = model.transcribe(audio_path)

    text = result["text"].strip()

    print("Heard:", text)

    return text
