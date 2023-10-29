# Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.

def isDivisibleBy3and4(start, end):
    for num in range(start, end + 1):
        if num % 3 == 0 and num % 4 == 0:
            yield num

start = 0
end = int(input("Enter the value of n: "))
numbers = list(isDivisibleBy3and4(start, end))
print(numbers)