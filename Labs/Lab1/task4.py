# 4. Digital clocks
n = int(input())
h = n // 60
m = n % 60

if(h > 23 and h < 25):
    print(0, m)
elif(h >= 25):
    print(h % 24, m)
else:
    print(h, m)