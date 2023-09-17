# 1. The sum of three numbers
a = int(input())
b = int(input())
c = int(input())

print(a + b + c)

# 2. Area of rectangle 
b = int(input())
h = int(input())

print((b * h) // 2)

# 3. Apple dividing 
n = int(input())
k = int(input())

print(k // n)
print(k % n)

# 4. Digital clocks
n = int(input())
h = n // 60
m = n % 60

if(h > 23 and h < 25):
    print(0, m)
elif(h >= 25):
    print(h % 24, m)
else:
    print(h, m)

# 5. Hello, Harry!
word = input()

print('Hello, ' +word+ '!')

# 6. Previous and next number
a = int(input())
b = a + 1
c = a - 1

print('The next number for the number ', a, 'is ', b)
print('The previous number for the number ', a, 'is ', c)

# 7. Desks
a = int(input())
b = int(input())
c = int(input())

print((a // 2) + (a % 2) + (b // 2) + (b % 2) + (c // 2) + (c % 2))

# 8. Laces
a = int(input())
b = int(input())
l = int(input())
N = int(input())

print(2 * l + (2 * N - 1) * a + 2 * (N - 1) * b)

