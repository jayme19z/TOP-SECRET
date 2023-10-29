# Write a Python program to calculate the area of a trapezoid.

a = float(input("Enter the value of the first side of the trapezoid: "))
b = float(input("Enter the value of the second side of the trapezoid: "))
h = float(input("Enter the value of the height of the trapezoid: "))

area = (0.5 * (a + b)) * h

print("The area of the trapezoid is", area)