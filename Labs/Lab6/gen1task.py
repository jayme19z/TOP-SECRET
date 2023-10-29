# Create a generator that generates the squares of numbers up to some number N.

def gen(n):
    num = 0
    while(num < n + 1):
        yield num * num
        num += 1

n = int(input())

for num in gen(n):
    print(num, end= ' ')