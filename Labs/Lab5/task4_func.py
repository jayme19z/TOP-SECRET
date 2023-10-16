# You are given list of numbers separated by spaces. Write a function 
# filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def filter_prime(numbers):
    prime_numbers = [number for number in numbers if is_prime(number)]
    return prime_numbers

input_numbers = input()
numbers = [int(num) for num in input_numbers.split()]
result = filter_prime(numbers)
print(result)