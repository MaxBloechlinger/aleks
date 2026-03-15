import pyttsx3

engine = pyttsx3.init()

speaking = False


def speak(text):
    global speaking

    speaking = True
    print(f"Aleks: {text}")

    engine.say(text)
    engine.runAndWait()

    speaking = False
