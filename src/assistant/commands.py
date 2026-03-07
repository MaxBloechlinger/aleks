def handle_command(text):
    text = text.lower()

    if "hello" in text:
        return "Hello Max."

    if "time" in text:
        return "I cannot tell the time yet."

    return "I don't understand yet."