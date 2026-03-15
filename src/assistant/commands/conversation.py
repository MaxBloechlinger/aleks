from datetime import datetime
from .router import register


def greet(text):
    hour = datetime.now().hour

    if 5 <= hour < 12:
        return "Good Morning Sire. May your day be prosperous."

    elif 12 <= hour < 18:
        return "Good Afternoon Sire."

    elif 18 <= hour < 23:
        return "Good Evening Sire."

    else:
        return "Working late tonight, Sire."

def who(text):
    return "I'm Aleks, your assistant."


def thanks(text):
    return "You're welcome Sire"


register(["hello", "hi", "good morning", "good evening", "good afternoon"], greet)
register(["who"], who)
register(["thanks", "thank you"], thanks)
