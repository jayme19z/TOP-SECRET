# Write a Python program with builtin function that checks whether a passed string is palindrome or not.

def isPalindrome(word):
    rev = ''.join(reversed(word))
    if (word == rev):
        return True
    return False

word = input()
check = isPalindrome(word)
 
if (check):
    print(word, 'is palindrome')
else:
    print(word, 'is not palindrome')




# def isPalindrome(x):
#     txt = x.lower()
#     rev = txt[::-1]
#     if(txt == rev):
#         return True
#     else:
#         return False

# x = input() 
# if(isPalindrome(x)):
#     print(x,'is palindrome')
# else:
#     print(x,'is not palindrome')