import re

with open('row.txt', 'r', encoding="utf8") as file:
    txt = file.readlines()

def findAa(line):
    x = re.findall("[A-Z][a-z]+", line)
    print(x)

for line in txt:
    findAa(line)