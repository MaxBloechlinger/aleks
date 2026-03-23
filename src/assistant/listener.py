import sounddevice as sd
import whisper
import tempfile
import wave
import time

from assistant.speaker import speaking_event, last_spoken_time

model = whisper.load_model("tiny.en")


def listen():

    # hard block while speaking
    if speaking_event.is_set():
        time.sleep(0.1)
        return None

    # cooldown after speech
    if time.time() - last_spoken_time < 2.5:
        time.sleep(0.1)
        return None

    samplerate = 16000
    duration = 2.5

    try:
        recording = sd.rec(
            int(duration * samplerate),
            samplerate=samplerate,
            channels=1,
            dtype="int16"
        )

        sd.wait()

        # speaking started while recording
        if speaking_event.is_set():
            return None

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
            with wave.open(f.name, "wb") as wf:
                wf.setnchannels(1)
                wf.setsampwidth(2)
                wf.setframerate(samplerate)
                wf.writeframes(recording.tobytes())

            audio_path = f.name

        result = model.transcribe(audio_path, fp16=False)

        text = result["text"].strip().lower()

        if not text:
            return None

        print("Heard:", text)
        return text

    except Exception as e:
        print("Audio error:", e)
        time.sleep(0.5)
        return None