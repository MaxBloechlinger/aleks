import pyttsx3
import time

engine = pyttsx3.init()

speaking = False
last_spoken_time = 0


def speak(text):
    global speaking, last_spoken_time

    speaking = True
    print(f"Aleks: {text}")

    engine.say(text)
    engine.runAndWait()

    speaking = False
    last_spoken_time = time.time()


def stop():
    global speaking
    engine.stop()
    speaking = False