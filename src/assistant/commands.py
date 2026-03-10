from datetime import datetime

def handle_command(text):
    text = text.lower()

    if "hello" in text:
        return "Hello Sir"

    if "time" in text:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        return f"It is {current_time}."
    
    if "who" in text:
        return "I'm Aleks, your assistant."
    
    if "Aleks" or "Alex" in text:
        return "hmm what?"

    return "I don't understand yet."