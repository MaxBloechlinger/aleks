from assistant.brain import process_command
from assistant.listener import listen

def print_manual():
    print("""
==============================
 Aleks Voice Assistant
==============================
Speak a command after you hear "Listening...".

Example commands:
 - "what time is it"
 - "exit" or "stop" to quit

Tips:
 - Speak clearly
 - Wait for "Listening..." before talking
 - Short sentences work best
==============================
""")

def main():
    print("Assistant booting up... (voice mode)")
    print_manual()

    while True:
        text = listen()

        if not text:
            continue

        if text.lower() in ["exit", "quit", "stop"]:
            print("Shutting down. Bye.")
            break

        response = process_command(text)
        print("Assistant:", response)

if __name__ == "__main__":
    main()