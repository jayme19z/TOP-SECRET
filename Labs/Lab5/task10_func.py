# Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set.

def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

user_input = input()
input_list = [int(item) for item in user_input.split()]

result = unique_elements(input_list)
print(result)