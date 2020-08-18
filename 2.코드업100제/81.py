a,b=map(int,input().split())
for i in range(1, a+1):
    c=1
    while b>=c:
        print(i,c)
        c+=1
    
for i in range(1,a+1):
    for k in range(1,b+1):
        print(i,k)
