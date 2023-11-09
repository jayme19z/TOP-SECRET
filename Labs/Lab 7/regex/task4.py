import re

def findAa():
    txt = input()
    x = re.findall("[A-Z][a-z]+", txt)
    print(x)

findAa()

