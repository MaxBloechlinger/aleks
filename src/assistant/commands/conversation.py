from .router import register


def hello(text):
    return "Hello Sir"

def good_morning(text):
    return "Good Morning Me Lord. May your highness have a splendid Day."


def who(text):
    return "I'm Aleks, your assistant."


def thanks(text):
    return "You're welcome Sire"


register(["hello"], hello)
register(["good morning"], good_morning)
register(["who"], who)
register(["thanks", "thank you"], thanks)
