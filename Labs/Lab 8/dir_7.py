# Write a Python program to copy the contents of a file to another file

def copyPaste():
    path = r'C:\Users\kozha\OneDrive\Рабочий стол\edu\Programming Principles II\Lab 8\hi.txt'
    pathOfSecondfile = r'C:\Users\kozha\OneDrive\Рабочий стол\edu\Programming Principles II\Lab 8\by.txt'

    f = open(path, "r")
    f1 = open(pathOfSecondfile, "w")

    for i in f:
        f1.write(str(i))
    f1.close()
    f.close()

    f1 = open(pathOfSecondfile, "r")
    for i in f1:
        print(i)

copyPaste()