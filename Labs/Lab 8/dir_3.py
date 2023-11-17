# Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.

import os

def existsOrNot(fname):
    if os.path.exists(fname):
        return True
    else:
        return False
    
myPath = r'C:\Users\kozha\OneDrive\Рабочий стол\edu\Programming Principles II\Lab 8\hi.txt'
print(existsOrNot(myPath))
print(myPath)