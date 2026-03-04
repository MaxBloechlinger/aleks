def process_command(text: str) -> str:
    if "time" in text.lower():
        return "I can't tell time yet."
    return "Command received."