import requests
import datetime

# weather code mapping from Open-Meteo
WEATHER_CODES = {
    0: "clear sky",
    1: "mainly clear",
    2: "partly cloudy skies",
    3: "cloudy skies",
    45: "foggy conditions",
    48: "depositing rime fog",
    51: "light drizzle",
    53: "moderate drizzle",
    55: "dense drizzle",
    61: "light rain",
    63: "moderate rain",
    65: "heavy rain",
    71: "light snowfall",
    73: "moderate snowfall",
    75: "heavy snowfall",
    80: "rain showers",
    81: "heavy rain showers",
    95: "a thunderstorm",
}


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
    code = data["current_weather"]["weathercode"]

    condition = WEATHER_CODES.get(code, "unknown weather")


    hour = datetime.datetime.now().hour

    if condition == "clear sky" and (hour >= 21 or hour <= 5):
        condition = "a starry night"


    return f"It is currently {temp} degrees with {condition}."
