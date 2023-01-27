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

from datetime import datetime
today = datetime.now()
t = today.strftime("%H:%M:%S")
print("time: ", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
print("time one: ", time_one)

#dd/mm/YY H:M:S format 

time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
print("time_two: ", time_two)

#retrieve / using date from datetime

from datetime import date 
d = date(2023, 1, 27)
print(d)
print("Current date: ", d.today)
today = date.today()
print("Current year: ", today.year)
print("Current month: ", today.month)
print("Current day: ", today.day)

# difference between two points in Time using timedelta function in Py

from datetime import timedelta 

t1 = timedelta(weeks=20, days=10, hours=6, seconds=25)
t2 = timedelta(days=8, hours=4, minutes=3, seconds=30)
t3 = t1 - t2 
print("t3 as time delta: ", t3)

# for timezone 

import datetime
import pytz

# using now() to get the current time & represent the output in timezone

current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))

# printing the current time now
print("The current local time is: ", current_time)







