a = set(str(i) for i in range(1, int(input()) + 1))
b = input()
while b != 'HELP':
    b = set(b.split())
    if len(a & b) > len(a - b):
        a = a & b
        print('YES')
    else:
        a = a - b
        print('NO')
    b = input()
print(*a)