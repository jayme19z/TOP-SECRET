import re

def splitUpper2():
    txt = input()
    x = re.sub(r"([A-Z][a-z]+)", r" \1", txt).strip()
    print(x)

splitUpper2()

