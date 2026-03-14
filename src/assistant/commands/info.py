from datetime import datetime
from .router import register
from assistant.weather import get_weather


def get_time(text):
    now = datetime.now()
    return f"It is {now.strftime('%H:%M')}."


def get_day(text):
    now = datetime.now()
    return f"It is {now.strftime('%A %d. of %B %Y')}."


register(["time"], get_time)
register(["day", "date"], get_day)
register(["weather"], lambda text: get_weather())
