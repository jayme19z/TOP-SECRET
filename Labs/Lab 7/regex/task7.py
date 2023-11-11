import re

with open('row.txt', 'r', encoding="utf8") as f:
    txt = f.read()

def snakeToCamel(txt):
    words = txt.split("_")
    camel_case = ''.join([words[0].lower()] + [word.capitalize() for word in words[1:]])
    return camel_case

t = snakeToCamel(txt)

with open('secondex.txt', 'w') as fr:
    fr.write(t)