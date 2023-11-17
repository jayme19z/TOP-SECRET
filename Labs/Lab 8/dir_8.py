# Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.

import os

def delitingFileInSpecificPath():
    path = r'C:\Users\kozha\OneDrive\Рабочий стол\edu\Programming Principles II\Lab 8\by.txt'
    if(os.access(path, os.F_OK)):
        print("Your path exist!\nOkay...let me delete your file")
        os.remove(path)
        print("Deleting is succesful! :D")
    else:
        print("Your path does not exist :(")

delitingFileInSpecificPath()