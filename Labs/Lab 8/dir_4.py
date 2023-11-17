# Write a Python program to count the number of lines in a text file.
import os

def countingLines():
    path = r'C:\Users\kozha\OneDrive\Рабочий стол\edu\Programming Principles II\Lab 8\hi.txt'
    f = open(path, "r")
    count = 0
    for i in f:
        if(i != "\n"):
            count += 1
    print("The amount of lines in this file is:", count)

countingLines()
