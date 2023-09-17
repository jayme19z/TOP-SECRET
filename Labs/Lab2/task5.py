# 5. minimum of three
a = int(input())
b = int(input())
c = int(input())

if(a == b or b == c or c == a):
    if(a == b):
        if(a < c):
            print(a)
        else:
            print(c)
    elif(b == c):
        if(b < a):
            print(b)
        else:
            print(a)
    else:
        if(a < c):
            print(a)
        else:
            print(c)
else:
    if(a < b and a < c):
        print(a)
    elif(b < a and b < c):
        print(b)
    else:
        print(c)