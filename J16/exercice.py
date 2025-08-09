"""Day16 30 days of Python Programming"""

from datetime import datetime, date, time


#1
now = datetime.now()
day=now.day
month=now.month
year=now.year
hour=now.hour
minute=now.min
timestamp=now.timestamp()

print("day:", day)
print("month:", month)
print("year:", year)
print("hour:", hour)
print("minute:", minute)
print("timestamp:", timestamp)

#2
print("currently:", now.strftime("%m/%d/%Y, %H:%M:%S"))

#3
date_string="5 December 2019"
converted=datetime.strptime(date_string, "%d %B %Y")
print(converted)

#4
diff=now - converted
print(diff)

#5
diff_from_1970 = now - datetime.fromtimestamp(0)
print(diff_from_1970)

#6
"""
invoices, billings
use date to notify user on expiration
coming soon
"""