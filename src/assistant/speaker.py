import pyttsx3
import time
import threading

engine = pyttsx3.init()

speaking_event = threading.Event()
last_spoken_time = 0


def speak(text):
    global last_spoken_time

    speaking_event.set()

    print(f"Aleks: {text}")

    engine.say(text)
    engine.runAndWait()

    last_spoken_time = time.time()
    speaking_event.clear()


def stop():
    engine.stop()
    speaking_event.clear()