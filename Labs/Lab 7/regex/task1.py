import re

def zeroOrMoreB(line):
    x = re.findall("ab*", line)
    print(x)

with open('row.txt', 'r', encoding="utf8") as file:
    for line in file:
        zeroOrMoreB(line)