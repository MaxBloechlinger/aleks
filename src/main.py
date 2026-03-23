import time
import threading
from queue import Queue

from assistant.listener import listen
from assistant.brain import think
from assistant.speaker import speak, stop
from assistant.wakeword import wait_for_wake_word


command_queue = Queue()

SESSION_TIMEOUT = 8
listening_enabled = False


def listener_loop():
    global listening_enabled

    while True:

        if not listening_enabled:
            time.sleep(0.1)
            continue

        text = listen()

        if not text:
            continue

        command_queue.put(text)


def main():

    global listening_enabled

    threading.Thread(target=listener_loop, daemon=True).start()

    print("Aleks voice assistant started")

    while True:

        wait_for_wake_word()

        speak("Yes Sire.")

        time.sleep(1.2) #prevent reaction to Yes Sire

        listening_enabled = True
        session_start = time.time()

        while time.time() - session_start < SESSION_TIMEOUT:

            try:
                text = command_queue.get(timeout=0.5)
            except:
                continue

            if "stop" in text:
                stop()
                continue

            if "exit" in text:
                speak("Shutting down.")
                return

            if "sleep" in text:
                speak("Returning to standby.")
                break

            response = think(text)
            speak(response)

            session_start = time.time()

        listening_enabled = False
        print("Returning to standby...")


if __name__ == "__main__":
    main()