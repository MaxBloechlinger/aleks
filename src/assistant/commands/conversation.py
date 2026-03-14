from .router import register


def hello(text):
    return "Hello Sir"


def who(text):
    return "I'm Aleks, your assistant."


def thanks(text):
    return "You're welcome Sire"


register(["hello"], hello)
register(["who"], who)
register(["thanks", "thank you"], thanks)
