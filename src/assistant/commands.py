from datetime import datetime
from assistant.weather import get_weather

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

    if any(word in text for word in ["day", "date"]):
        now = datetime.now()
        current_day = now.strftime("%A %d. of %B %Y")
        return f"It is {current_day}."

    if any(word in text for word in ["thanks", "thank you"]):
        return "You're welcome Sire"

    if any(word in text for word in ["alex", "aleks"]):
        return "Hmm, what?"

    if "weather" in text:
        return get_weather()

    return "I don't understand yet."
