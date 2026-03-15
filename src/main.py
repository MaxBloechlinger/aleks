from assistant.listener import listen
from assistant.brain import think
from assistant.speaker import speak, stop_speaking
from assistant.wakeword import is_wake_word


def main():
    print("Aleks voice assistant started")
    print("Say 'Aleks' to wake me.\n")

    while True:

        # --- WAIT FOR WAKE WORD ---
        text = listen()

        if not text:
            continue

        if "exit" in text.lower():
            speak("Shutting down. Goodbye.")
            break

        if not is_wake_word(text):
            continue

        speak("Yes Sire?")

        # --- COMMAND MODE ---
        command = listen()

        if not command:
            continue

        if command in ["stop", "wait", "cancel"]:
            stop_speaking()
            continue

        if "exit" in command:
            speak("Shutting down. Goodbye.")
            break

        response = think(command)
        speak(response)


if __name__ == "__main__":
    main()
