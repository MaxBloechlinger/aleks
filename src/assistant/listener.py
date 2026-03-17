import sounddevice as sd
import numpy as np
import whisper
import webrtcvad
import tempfile
import wave
import collections

from assistant.speaker import speaking, last_spoken_time
import time

model = whisper.load_model("base")

vad = webrtcvad.Vad(2)  # 0-3 (higher = more aggressive)

SAMPLE_RATE = 16000
FRAME_DURATION = 30  # ms
FRAME_SIZE = int(SAMPLE_RATE * FRAME_DURATION / 1000)


def listen():

    # wait if Aleks is speaking
    while speaking:
        time.sleep(0.1)

    # small cooldown to avoid echo
    while time.time() - last_spoken_time < 1.0:
        time.sleep(0.1)

    print("Listening...")

    audio_buffer = []
    ring_buffer = collections.deque(maxlen=10)

    stream = sd.InputStream(
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16",
        blocksize=FRAME_SIZE
    )

    with stream:

        triggered = False

        while True:
            frame, _ = stream.read(FRAME_SIZE)
            frame_bytes = frame.tobytes()

            is_speech = vad.is_speech(frame_bytes, SAMPLE_RATE)

            if not triggered:
                ring_buffer.append((frame_bytes, is_speech))

                # start when enough speech detected
                if sum(1 for _, speech in ring_buffer if speech) > 6:
                    triggered = True
                    audio_buffer.extend(f for f, _ in ring_buffer)
                    ring_buffer.clear()

            else:
                audio_buffer.append(frame_bytes)
                ring_buffer.append((frame_bytes, is_speech))

                # stop when silence detected
                if sum(1 for _, speech in ring_buffer if not speech) > 8:
                    break

    if not audio_buffer:
        return ""

    # save temp audio
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        with wave.open(f.name, "wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(SAMPLE_RATE)
            wf.writeframes(b"".join(audio_buffer))

        audio_path = f.name

    result = model.transcribe(audio_path)

    text = result["text"].strip().lower()

    print("Heard:", text)

    # filter self-hearing
    from assistant.speaker import last_spoken_text
    if text and text in last_spoken_text:
        return ""

    return text
