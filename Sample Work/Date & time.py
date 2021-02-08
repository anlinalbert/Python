# Date & time functions

import datetime
from datetime import date, timedelta

print("1. Get current time\n2. Current date minus 5\n3. Print yesterday, today & tomorrow\n4. Print next 5 days\n5. Add 5 seconds to current time")
try :
    c = int(input("\nChoice = "))
    print()

    if c == 1 :
        now = datetime.datetime.now()
        current = now.strftime("%H:%M:%S")
        print("Time:", current)
    elif c == 2 :
        print("Date - 5:", date.today() - timedelta(5))
    elif c == 3 :
        print("Yesterday:", date.today() - timedelta(1), "\nToday:", date.today(), "\nTomorrow:", date.today() + timedelta(1))
    elif c == 4 :
        print("Next 5 days:")
        for x in range(1, 6) :
            print(date.today() + timedelta(x))
    elif c == 5 :
        now = datetime.datetime.now()
        current = now.strftime("%H:%M:%S")
        print("Current time:", current)
        now = datetime.datetime.now() + timedelta(0, 5)
        current = now.strftime("%H:%M:%S")
        print("Time + 5 sec:", current)
except :
    print("Error")