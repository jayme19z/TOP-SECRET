# 1. Minimum 
a = int(input())
b = int(input())

if(a > b):
    print(b)
else:
    print(a)

# 2. Number's sign
x = int(input())

if x > 0:
    print(1)
elif x == 0:
    print(0)
else:
    print(-1)

# 3. Chess
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if((a1 + b1 + a2 + b2) % 2 == 0):
    print('YES')
else:
    print('NO')

#4. Leap year
y = int(input())

if((y % 4 == 0 and y % 100 != 0) or y % 400 == 0):
    print('YES')
else:
    print('NO')

# 5. minimum of three
a = int(input())
b = int(input())
c = int(input())

if(a == b or b == c or c == a):
    if(a == b):
        if(a < c):
            print(a)
        else:
            print(c)
    elif(b == c):
        if(b < a):
            print(b)
        else:
            print(a)
    else:
        if(a < c):
            print(a)
        else:
            print(c)
else:
    if(a < b and a < c):
        print(a)
    elif(b < a and b < c):
        print(b)
    else:
        print(c)
    
# 6. How many numbers match
a = int(input())
b = int(input())
c = int(input())

if(a == b == c):
    print(3)
elif(a == b or b == c or a == c):
    print(2)
else:
    print(0)

# 7. The Rook's move
a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())

if(a1 == b1 or a2 == b2):
    print('YES')
else:
    print('NO')
 
# 8. The King's move
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if (abs(a1 - a2) <= 1 and abs(b1 - b2) <= 1):
    print('YES')
else:
    print('NO')

# 9. The Bishop's move
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if abs(a2 - a1) == abs(b2 - b1):
    print('YES')
else:
    print('NO')
 
# 10. The Queen's move
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if(abs(a1 - a2) == abs(b1 - b2) or a1 == a2 or b2 == b1):
    print('YES')
else:
    print('NO')

# 11. The Knight's move
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if((abs(a1 - a2) == 1 or abs(a1 - a2) == 2) and (abs(b1 - b2) == 1 or abs(b1 - b2) == 2) and (abs(b1 - b2)) != (abs(a1 - a2))):
    print('YES')
else:
    print('NO')

# 12. The chocolate
n = int(input())
m = int(input())
k = int(input())

if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')

# 13. Yasha is swimming in the pool
N = int(input())
M = int(input())
x = int(input())
y = int(input())

if N > M:
    N, M = M, N
if x >= N / 2:
    x = N - x
if y >= M / 2:
    y = M - y

if x < y:
    print(x)
else:
    print(y)
    