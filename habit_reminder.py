import time
import os
from datetime import datetime

habits = {
    "Hydrate",
    "Move",
    "Meditate",
    "Piano",
    "Code"
}

def remind_daily(habit, hour, minute):
    now = datetime.now()
    already_notified = False
    while True:
        if now.hour == hour and now.minute == minute:
            if not already_notified:
                already_notified = True
                print("Sending Notif")
                os.system(
                        f'''osascript -e 'display dialog "{habit}" buttons {{"OK"}} with title "Daily Reminder"' '''
                    )
        time.sleep(60)
remind_daily("Drink", 18, 30)