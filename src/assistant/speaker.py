import pyttsx3

engine = pyttsx3.init()

speaking = False
last_spoken_text = ""


def speak(text):
    global speaking, last_spoken_text

    speaking = True
    last_spoken_text = text.lower()

    print(f"Aleks: {text}")

    engine.say(text)
    engine.runAndWait()

    speaking = False


def stop_speaking():
    engine.stop()
