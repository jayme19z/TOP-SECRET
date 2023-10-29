#Write a Python program to calculate two date difference in seconds.
import datetime

d1 = datetime.datetime.now()

print("Enter the year")
x = int(input())
print("Enter the month")
y = int(input())
print("Enter the day")
z = int(input())

d2 = datetime.datetime(year= x, month= y, day= z)

delta = d1 - d2
print(delta.total_seconds())