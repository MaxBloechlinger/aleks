from assistant.listener import listen
from assistant.brain import think
from assistant.speaker import speak, stop_speaking
from assistant.wakeword import wait_for_wake_word



def main():
    print("Aleks voice assistant started")

    while True:

        wait_for_wake_word()

        speak("Yes Sire")

        text = listen()

        if not text:
            continue

        if "exit" in text:
            speak("Shutting down.")
            break

        response = think(text)

        speak(response)



if __name__ == "__main__":
    main()
