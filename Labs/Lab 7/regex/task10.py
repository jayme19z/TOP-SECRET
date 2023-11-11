import re

with open('row.txt', 'r', encoding="utf8") as f:
    txt = f.read()

def camelToSnake(txt):  
    x = re.sub(r"([A-Z][a-z]+)", r" \1", txt).strip()
    x = x.split(' ')
    s = ''
    for i in range(0, len(x)):
        s += x[i].lower() + '_'
    return s[:-1] 

t = camelToSnake(txt)

with open('fifthex.txt', 'w') as fr:
    fr.write(t)