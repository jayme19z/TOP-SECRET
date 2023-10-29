# Write a Python program to convert degree to radian.
import math

# Method 1: Using the math.radians function
x = float(input("Enter the angle in degrees: "))
rad = math.radians(x)
print("The result is", rad)

# Method 2: Direct calculation using the pi
degree = float(input("Enter the angle in degrees: "))
radian = degree * (math.pi/180)
print("The result is", radian)
