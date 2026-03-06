import pyttsx3

engine = pyttsx3.init()

def speak(text: str):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()
    