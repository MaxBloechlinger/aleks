from assistant.brain import process_command
from assistant.listener import listen
from assistant.speaker import speak


def print_manual():
    print("""
==============================
 Aleks Voice Assistant
==============================
Speak after 'Listening...'
Say 'exit' to stop
==============================
""")


def main():
    print("Assistant booting up...")
    print_manual()

    while True:
        text = listen()

        if not text:
            continue

        if text.lower() in ["exit", "quit", "stop"]:
            speak("Shutting down. Goodbye.")
            break

        response = process_command(text)
        speak(response)


if __name__ == "__main__":
    main()