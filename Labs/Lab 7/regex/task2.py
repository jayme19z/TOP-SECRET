import re

def twoORthree():
    txt = input()
    x = re.findall("ab{2,3}", txt)
    print(x)

twoORthree()
