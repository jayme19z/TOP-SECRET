import re

with open('row.txt', 'r', encoding="utf8") as file:
    txt = file.readlines()

def sequenceOfLowerLetters(line):
    l = []
    line = line.strip()
    for i in range(0, len(line) - 1):
        x1 = re.search("[a-z]", line[i])
        x2 = re.search("[a-z]", line[i + 1])
        if x1 and x2:
            l.append(line[i] + "_" + line[i + 1])
    print(l)

for line in txt:
    sequenceOfLowerLetters(line)