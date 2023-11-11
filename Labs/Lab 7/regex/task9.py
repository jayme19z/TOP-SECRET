import re

with open('row.txt', 'r', encoding="utf8") as f:
    txt = f.read()

def splitUpper2(txt):
    x = re.sub(r"([A-Z][a-z]+)", r" \1", txt).strip()
    return x

t = splitUpper2(txt)

with open('fourthex.txt', 'w') as fr:
    fr.write(t)