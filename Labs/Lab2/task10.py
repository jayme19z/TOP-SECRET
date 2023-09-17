# 10. The Queen's move
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if(abs(a1 - a2) == abs(b1 - b2) or a1 == a2 or b2 == b1):
    print('YES')
else:
    print('NO')