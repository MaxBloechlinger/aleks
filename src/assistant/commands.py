from datetime import datetime
import requests


def get_weather():
    lat = 47.3769
    lon = 8.5417

    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}&current_weather=true"
    )

    r = requests.get(url)
    data = r.json()

    temp = data["current_weather"]["temperature"]
    wind = data["current_weather"]["windspeed"]

    return f"It is {temp} degrees Celsius with wind speed {wind} kilometers per hour."


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
