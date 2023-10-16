# Write a function that accepts string from user and print all permutations of that string.

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

user_input = input()
for permuted_string in gen_permut(user_input):
    print(permuted_string)