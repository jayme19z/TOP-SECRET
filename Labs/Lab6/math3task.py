# Write a Python program to calculate the area of regular polygon.

a = float(input("Enter the value of the side of the regular polygon: "))
r = float(input("Enter the value of the inscribed circle radius of the regular polygon: "))
n = int(input("Enter the number of the angles of the regular polygon: "))

p = n * a #perimeter
area = 0.5 * p * r

print("The area of the regular polygon is", area)