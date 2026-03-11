# Just for fun, lets try building a chatbot from the ground up
# that gives us random quotes.

import requests

api_link = "https://uselessfacts.jsph.pl/random.json"

def get_fact() -> str:
    json_data = requests.get(api_link).json()
    return json_data['text']


