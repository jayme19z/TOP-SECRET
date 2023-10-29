#Write a Python program to print yesterday, today, tomorrow.
import datetime

today = datetime.datetime.now()
delta = datetime.timedelta(days=1)
yesterday = today - delta
tomorrow = today + delta

print("Yesterday is", yesterday.date())
print("Today is", today.date()) 
print("Tomorrow is", tomorrow.date())