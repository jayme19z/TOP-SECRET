import re

def zeroOrMoreB():
    txt = input()
    x = re.findall("ab*", txt)
    print(x)

zeroOrMoreB()

