# Functions
# 1
def otog(g):
    oz = g / 28.3495231
    print(oz)

# 2
def ftoc(f):
    c = (5 / 9) * (f - 32)
    print(c)

# 3
def solve(numheads, numlegs):
    rabbit = (numlegs - 2*numheads) / 2
    chicken = numheads - rabbit
    print("Number of rabbits: ", rabbit, "\nNumber of chickens: ", chicken)

# 4
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

# 5
def gen_permut(input_string):
    if len(input_string) == 0:
        return [""]
    
    permut = []
    for i in range(len(input_string)):
        char = input_string[i]
        remaining_chars = input_string[:i] + input_string[i+1:]
        for perm in gen_permut(remaining_chars):
            permut.append(char + perm)
    
    return permut

# 6
def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = " ".join(reversed_words)
    return reversed_sentence

# 7
def has33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

# 8
def contains007(nums):
    if len(nums) < 3:
        return False

    for i in range(len(nums) - 2):
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 7:
            return True

    return False

# 9
import math

def sphere_volume(r):
    if r < 0:
        return "Radius cannot be negative."
    v = (4/3) * math.pi * (r**3)
    return v

# 10
def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# 11
def is_palindrome(word):
    clean_word = ''.join(word.split()).lower()
    return clean_word == clean_word[::-1]

# 12
def histogram(data):
    for value in data:
        bar = '*' * value
        print(bar)

# 13
import random

def guess_the_number():
    secret_number = random.randint(1, 20)
    max_attempts = 100

    print("Welcome to the 'Guess the Number' game!")
    player_name = input("Please enter your name: ")

    print(f"Hello, {player_name}! I'm thinking of a number between 1 and 20.")

    for attempts in range(max_attempts):
        guess = int(input("Take a guess: "))

        if guess < secret_number:
            print("Your guess is too low")
        elif guess > secret_number:
            print("Your guess is too high")
        else:
            print(f"Good job, {player_name}! You guessed my number in {attempts + 1} attempts!")
            return

    print(f"Sorry, {player_name}, you've run out of attempts. The secret number was {secret_number}.")


# Main
# 1
g = float(input())
otog(g)

# 2
f = int(input())
ftoc(f)

# 3
numheads = 35
numlegs = 94
solve(numheads, numlegs)

# 4
input_numbers = input()
numbers = [int(num) for num in input_numbers.split()]
result = filter_prime(numbers)
print(result)

# 5
user_input = input()
for permuted_string in gen_permut(user_input):
    print(permuted_string)

# 6
user_input = input()
reversed_sentence = reverse_words(user_input)
print(reversed_sentence)

# 7
user_input = input()
num_list = [int(num) for num in user_input.split()]

result = has33(num_list)
print(result)

# 8
user_input = input()
num_list = [int(num) for num in user_input.split()]

result = contains007(num_list)
print(result)

# 9
r = float(input())
result = sphere_volume(r)
print(result)

# 10 
user_input = input()
input_list = [int(item) for item in user_input.split()]

result = unique_elements(input_list)
print(result)

# 11
user_input = input()
result = is_palindrome(user_input)

if result:
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")

# 12
user_input = input()
input_data = [int(num) for num in user_input.split()]

histogram(input_data)

# 13
guess_the_number()
