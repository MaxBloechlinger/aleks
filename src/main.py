from assistant.brain import process_command

def main():
    print("Assistant booting up...")
    while True:
        command = input("You: ")
        if command.lower() in ["exit", "quit"]:
            break
        response = process_command(command)
        print("Assistant:", response)

if __name__ == "__main__":
    main()