# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

import os

def AtxtToZtxt():
    path = r'C:\Users\kozha\OneDrive\Рабочий стол\edu\Programming Principles II\Lab 8'
    for i in range(65, 90):
        name = os.path.join(path, chr(i) +".txt")
        f = open(name, "a")
    for i in os.listdir(path):
        print(i)

AtxtToZtxt()