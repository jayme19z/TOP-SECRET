# Write a Python program to write a list to a file.

import os

def listToFile():
    path = r'C:\Users\kozha\OneDrive\Рабочий стол\edu\Programming Principles II\Lab 8\new.txt'
    my_list = ["Zhamilya" ",", "I am giving you", 10, "extra points!", "Good job!"]

    f = open(path, "w")
    print("Let me write this list to your file:\n")
    print(my_list)
    for i in my_list:
        f.write(str(i) + " ")
    f.close()

    f = open(path, "r")
    print(f.read())

listToFile()