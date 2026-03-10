def handle_command(text):
    text = text.lower()

    if "hello" in text:
        return "Hello Sir"

    if "time" in text:
        return "I cannot tell the time yet."
    
    if "who" in text:
        return "I'm Aleks, your assistant."
    
    if "Aleks" or "Alex" in text:
        return "hmm what?"

    return "I don't understand yet."