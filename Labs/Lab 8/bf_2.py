# Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters

def countAa():
    s = input()
    lower = 0
    upper = 0
    for i in s:
        if(ord(i) >= 65 and ord(i) <= 90):
            upper += 1
        elif(ord(i) >= 97 and ord(i) <= 122):
            lower += 1

    print('Number of lowercase letters:', lower)
    print('Number of uppercase letters:', upper)

countAa()

