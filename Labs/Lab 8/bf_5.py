# Write a Python program with builtin function that returns True if all elements of the tuple are true. 

def trueTuple():
    cnt = 0
    f = (0, True, 6, "LOL", 1, False)
    t = (1, True) 
    for i in t: # choose which one you want to check
        if(bool(i) == False):
            return False
    return True

print(trueTuple())