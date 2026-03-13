from datetime import datetime
from assistant.weather import get_weather


def say_hello(text):
    return "Hello Sir"


def get_time(text):
    now = datetime.now()
    return f"It is {now.strftime('%H:%M')}."


def who_are_you(text):
    return "I'm Aleks, your assistant."


def get_day(text):
    now = datetime.now()
    return f"It is {now.strftime('%A %d. of %B %Y')}."


def thanks(text):
    return "You're welcome Sire"


def wake(text):
    return "Hmm, what?"


COMMANDS = [
    (["hello"], say_hello),
    (["time"], get_time),
    (["who"], who_are_you),
    (["day", "date"], get_day),
    (["thanks", "thank you"], thanks),
    (["alex", "aleks"], wake),
    (["weather"], lambda text: get_weather()),
]


def handle_command(text):
    text = text.lower()

    for keywords, handler in COMMANDS:
        if any(word in text for word in keywords):
            return handler(text)

    return "I don't understand yet."
