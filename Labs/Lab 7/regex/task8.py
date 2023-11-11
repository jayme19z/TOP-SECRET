import re

with open('row.txt', 'r', encoding="utf8") as f:
    txt = f.read()

def split_at_upper(txt):
    x = re.findall(r'[a-z]+|[A-Z][a-z]*', txt)
    return ' '.join(x)

t = split_at_upper(txt)

with open('thirdex.txt', 'w') as fr:
    fr.write(t)