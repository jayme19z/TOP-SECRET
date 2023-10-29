#Write a Python program to subtract five days from current date.
import datetime 

x = datetime.datetime.now()
delta = datetime.timedelta(days=5)
print(x.date() - delta)
