import re

with open('row.txt', 'r', encoding="utf8") as file:
    txt = file.readlines()

def replace(line):
    modified_line = re.sub(r'[ ,.]', ':', line)
    print(modified_line)
    return modified_line

with open('firstex.txt', 'w') as fr:
    for line in txt:
        modified_line = replace(line)
        fr.write(modified_line)