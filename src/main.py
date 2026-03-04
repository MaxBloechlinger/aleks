from assistant.brain import process_command
from assistant.listener import listen

def main():
    print("Assistant booting up... (voice mode)")

    while True:
        text = listen()

        if not text:
            continue

        if text.lower() in ["exit", "quit", "stop"]:
            break

        response = process_command(text)
        print("Assistant:", response)

if __name__ == "__main__":
    main()