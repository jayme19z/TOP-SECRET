import re

def replace():
    txt = input()
    x = re.sub(r'[ ,.]', ':', txt)
    print(x)

replace()