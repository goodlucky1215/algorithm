a,b=map(int,input().split())
b=b-45
if b<0 and a==0:
    print(23,60+b)
elif b<0:
    print(a-1,60+b)
else:
    print(a,b)