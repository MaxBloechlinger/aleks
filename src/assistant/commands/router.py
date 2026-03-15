from assistant.ai import ask_llm

COMMANDS = []

def register(keywords, handler):
    COMMANDS.append((keywords, handler))


def handle_command(text):
    text = text.lower()

    for keywords, handler in COMMANDS:
        if any(word in text for word in keywords):
            return handler(text)

    # fallback to AI
    return ask_llm(text)
