import datetime
import sys
weekdays = {"Monday": 0, "Tuesday": 1, "Wednesday": 2,
            "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}
weekday = input()
if weekday not in weekdays.keys():
    print("Invalid Day")
    sys.exit()
day, month, year = (int(i) for i in input().split('/'))
date = datetime.datetime(1, 1, 1)
try:
    second = datetime.datetime(year, month, day)
except:
    print ("Invalid Date")
    sys.exit()
day = second.day
weekday = weekdays[weekday]
if weekday != 0:
    wd_diff = weekday
else:
    wd_diff = 0
total_days = (second - date).days
date = date + datetime.timedelta(days=total_days)
if second.weekday() + wd_diff != 5 or second.weekday() + wd_diff != 6 or (total_days % 4) == 0:
    if second.day <= 50:
        print(second.day)
    else:
        print (50)

else:
    print(0)
