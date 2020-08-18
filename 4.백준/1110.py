n=int(input())
a=n
b=n%10
c=(n//10+b)%10
n=int(str(b)+str(c))
d=1
while a!=n:
    b=n%10
    c=(n//10+b)%10
    n=int(str(b)+str(c))
    d+=1
print(d)
