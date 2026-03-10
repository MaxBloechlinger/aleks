import sounddevice as sd
import numpy as np
import whisper
import tempfile
import wave

model = whisper.load_model("base")


def listen():
    print("Listening...")

    samplerate = 16000
    duration = 5  # seconds

    recording = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    # save temporary wav file
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