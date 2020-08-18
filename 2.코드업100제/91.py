a, m, d, n = map(int,input().split())

f=1
while n-1>=f:
    a = a*m+d
    f+=1
    
print(a)
