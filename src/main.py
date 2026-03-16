import time
from assistant.listener import listen
from assistant.brain import think
from assistant.speaker import speak
from assistant.wakeword import wait_for_wake_word


SESSION_TIMEOUT = 8   # seconds Aleks stays active


def main():

    print("Aleks voice assistant started")

    while True:

        wait_for_wake_word()

        speak("Yes Sire.")

        session_start = time.time()

        while time.time() - session_start < SESSION_TIMEOUT:

            text = listen()

            if not text:
                continue

            if "exit" in text:
                speak("Shutting down.")
                return

            # ---- SLEEP COMMAND ----
            if "sleep" in text:
                speak("Returning to standby.")
                break
            # -----------------------

            response = think(text)
            speak(response)

            session_start = time.time()

        print("Returning to standby...")


if __name__ == "__main__":
    main()
