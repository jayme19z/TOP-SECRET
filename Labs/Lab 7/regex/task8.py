import re

def split_at_upper():
    x = input()
    txt = re.findall(r'[a-z]+|[A-Z][a-z]*', x)
    print(txt)

split_at_upper()