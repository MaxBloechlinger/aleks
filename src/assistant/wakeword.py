WAKE_WORDS = ["aleks", "alex"]

def is_wake_word(text: str) -> bool:
    text = text.lower()
    return any(word in text for word in WAKE_WORDS)
