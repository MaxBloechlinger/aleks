from assistant.listener import listen
from assistant.brain import think
from assistant.speaker import speak


def main():
    print("Aleks voice assistant started")

    text = listen()

    if text:
        response = think(text)
        speak(response)


if __name__ == "__main__":
    main()