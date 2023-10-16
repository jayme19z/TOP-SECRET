# Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20. This is how it should work when run in a terminal:

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

guess_the_number()
