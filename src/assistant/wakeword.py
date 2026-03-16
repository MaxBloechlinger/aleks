import pvporcupine
import pyaudio
import os


def wait_for_wake_word():

    porcupine = pvporcupine.create(
        access_key=os.environ["PICOVOICE_ACCESS_KEY"],
        keywords=["alexa"]
    )

    pa = pyaudio.PyAudio()

    stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )

    print("Waiting for wake word...")

    while True:
        pcm = stream.read(porcupine.frame_length)
        pcm = memoryview(pcm).cast("h")

        result = porcupine.process(pcm)

        if result >= 0:
            print("Wake word detected")
            break

    stream.close()
    pa.terminate()

    return True