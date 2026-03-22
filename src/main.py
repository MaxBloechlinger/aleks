import time
import threading
from assistant.listener import listen
from assistant.brain import think
from assistant.speaker import speak, stop, speaking, last_spoken_time, last_spoken_text
from assistant.wakeword import wait_for_wake_word
from queue import Queue

command_queue = Queue()


SESSION_TIMEOUT = 8   #Aleks stays active for 8 seconds

def listener_loop():
    while True:
        text = listen()

        if not text:
            continue

        text = text.lower()
        now = time.time()

        # FILTER 1: ignore while speaking
        if speaking:
            continue

        #  FILTER 2: cooldown after speaking 
        if now - last_spoken_time < 3.0:
            continue

        # FILTER 3: ignore similar text
        if last_spoken_text and any(word in text for word in last_spoken_text.split()):
            print("Ignored (self-echo):", text)
            continue

        print("Queue:", text)
        command_queue.put(text)


def main():
    threading.Thread(target=listener_loop, daemon=True).start()

    print("Aleks voice assistant started")

    while True:

        wait_for_wake_word()
        speak("Yes Sire.")

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

        print("Returning to standby...")


if __name__ == "__main__":
    main()
