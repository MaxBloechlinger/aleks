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

    if "day" or "date" in text:
        now = datetime.now()
        current_day = now.strftime("%A %d. of %B %Y")
        return f"It is {current_day}."
    
    if "thanks" or "thank" in text:
        return "You're welcome Sire"

    if "Aleks" or "Alex" in text:
        return "hmm what?"

    return "I don't understand yet."