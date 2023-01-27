# current date-time using Python
# in python, date & time are not data types on their own, but a built-in module named as DateTime can be imported
# to work with the date as well as time. 

# Datetime module comes built into python, there's no need to install it externally. To get both date and time
# datetime.now() function of the DateTime module. 

# Python datetime module to handle date and time

import datetime

x = datetime.date.today()
print(x)

# using now() to get the current time 
current_time = datetime.datetime.now()

print("Time is now in UTC and local time: ", current_time)

# retrieve datetime attributes 

#datetime.now has different attributes, same as attributes of time such as year, month, date, hour, minute and second. 

from datetime import datetime
now = datetime.now()
print(now)
# get the current day 
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()
print("The current day, month, year & hour, minute, second is: ", day, month, year, hour, minute, second, timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')


