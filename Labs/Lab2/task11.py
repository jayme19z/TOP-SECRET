# 11. The Knight's move
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if((abs(a1 - a2) == 1 or abs(a1 - a2) == 2) and (abs(b1 - b2) == 1 or abs(b1 - b2) == 2) and (abs(b1 - b2)) != (abs(a1 - a2))):
    print('YES')
else:
    print('NO')
