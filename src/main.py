from assistant.listener import listen
from assistant.brain import think
from assistant.speaker import speak


def main():
    print("Aleks voice assistant started")
    print("Say 'exit' to stop.\n")

    while True:
        text = listen()

        if not text:
            continue

        if "exit" in text.lower():
            speak("Shutting down. Goodbye.")
            break

        response = think(text)
        speak(response)


if __name__ == "__main__":
    main()