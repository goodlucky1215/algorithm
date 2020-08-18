a,r,n = map(int,input().split())
f=1
while n-1>=f:
    a*=r
    f+=1

print(a)
