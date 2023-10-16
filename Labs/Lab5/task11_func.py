# Write a Python function that checks whether a word or phrase is palindrome 
# or not. Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam

def is_palindrome(word):
    clean_word = ''.join(word.split()).lower()
    return clean_word == clean_word[::-1]

user_input = input()
result = is_palindrome(user_input)

if result:
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")