a=set(input().split())
b=set(input().split())
c=b&a
d=list(c)
for i in range (len(d)):
    d[i]=int(d[i])
a1=min(d)
a2=max(d)
for i in range (a1,a2+1):
    if i in d:
        print(i, end=' ')