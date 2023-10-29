# Implement a generator that returns all numbers from (n) down to 0.

def gen(start, end):
    while(start > end):
        yield start
        start = start - 1

start = int(input())
end = 0

for start in gen(start, end):
    print(start, end = ' ')