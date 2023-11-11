import re

with open('row.txt', 'r', encoding="utf8") as file:
    txt = file.readlines()

def startWithAEndWithB(line):
    x = re.findall("^a.*b$", line)
    print(x)

for line in txt:
    startWithAEndWithB(line)