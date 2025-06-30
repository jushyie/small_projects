import random
import time
import os
import requests

url = "https://zenquotes.io/api/quotes/"

def get_random_quote():
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        quotes = []
        for i in data:
            quotes.append(f'{i["q"]} - {i["a"]}')
        rand_quote = random.choice(quotes)
        return rand_quote
    else:
        return(f"Error {response.status_code}")


def display_quote(quote): 
    os.system(f''' osascript -e 'display dialog "{quote}" buttons {{"OK"}} with title "Motivation!"' ''')
    
def display_regularly(interval = 60): # hourly
    while True:
        quote = get_random_quote()
        display_quote(quote)
        time.sleep(interval * 60)
display_regularly()
