import wikipedia
import wolframalpha
from utils.tts import speak
from config import WOLFRAM_KEY


def search(query):
    c=wolframalpha.Client(WOLFRAM_KEY)
    res = c.query(query)
    return next(res.results)

print search("Weather in Stony Brook")