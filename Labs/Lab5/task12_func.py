# Define a functino histogram() that takes a list of integers and prints a histogram to the screen. 

def histogram(data):
    for value in data:
        bar = '*' * value
        print(bar)

user_input = input()
input_data = [int(num) for num in user_input.split()]

histogram(input_data)