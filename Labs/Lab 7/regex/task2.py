import re

with open('row.txt', 'r', encoding="utf8") as file:
    txt = file.readlines()

def twoORthree(line):
    x = re.findall("ab{2,3}", line)
    print(x)

for line in txt:
    twoORthree(line)