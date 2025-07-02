import os
import time
import random

# reminding to drink 6 times a day (8 - 20)
def remind_to_drink(liters):
    cupsize = (liters / 6) * 1000
    
    message = [
        "Good Morning.\nStart your day with some water! =^v^=",
        "It's a good time to drink a bit!",
        "Did you drink enough with your lunch?",
        "Hope you're hydrating well!",
        "Come on, take a sip now!",
        "How about a glass before bed?"
        ]

    for m in message:
        os.system(f''' osascript -e 'display dialog "{m}\n{cupsize} ml" buttons "OK" with title "Time to drink!"' ''')
        time.sleep(120 * 60)
remind_to_drink(1.5)
