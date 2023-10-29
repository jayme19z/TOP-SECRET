# Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.

def evenNumSepByComma(n):
    step = 2
    while step < n:
        yield str(step)
        step += 2
        if step < n: 
            yield ', '

n = int(input())    
for step in evenNumSepByComma(n):
    print(step, end = '')