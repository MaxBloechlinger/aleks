import sounddevice as sd
import numpy as np
import whisper
import tempfile
import wave
import time

# load whisper model once
model = whisper.load_model("base")

# --- shared state (imported from speaker) ---
try:
    from assistant.speaker import speaking, last_spoken_time, last_spoken_text
except:
    speaking = False
    last_spoken_time = 0
    last_spoken_text = ""


def listen():

    try:
        samplerate = 16000
        duration = 4  # slightly shorter = faster response

        # --- RECORD ---
        recording = sd.rec(
            int(duration * samplerate),
            samplerate=samplerate,
            channels=1,
            dtype="int16"
        )

        sd.wait()

        # --- SAVE TEMP FILE ---
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
            with wave.open(f.name, "wb") as wf:
                wf.setnchannels(1)
                wf.setsampwidth(2)
                wf.setframerate(samplerate)
                wf.writeframes(recording.tobytes())

            audio_path = f.name

        # --- TRANSCRIBE ---
        result = model.transcribe(audio_path, fp16=False)
        text = result["text"].strip().lower()

        if not text:
            return None

        now = time.time()

        # --- FILTER 1: ignore while speaking ---
        if speaking:
            return None

        # --- FILTER 2: cooldown after speaking ---
        if now - last_spoken_time < 4.0:
            return None

        # --- FILTER 3: ignore own voice ---
        if last_spoken_text:
            spoken_words = set(last_spoken_text.split())
            heard_words = set(text.split())

            overlap = spoken_words.intersection(heard_words)

            if len(overlap) > 2:
                print("Ignored (self-echo):", text)
                return None

        print("Heard:", text)
        return text

    except Exception as e:
        print("Audio error:", e)
        time.sleep(0.5)
        return None