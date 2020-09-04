n=int(input())
def find(a,m):
    b=[0]*m
    f=m-1
    b[m//2]=a[f]
    j=m//2
    k=m//2
    while j>0 and k<m-1:
        j-=1
        k+=1
        f-=1
        b[j]=a[f]
        f-=1
        b[k]=a[f]
    if m%2==0:
        j-=1
        f-=1
        b[j]=a[f]
    re=0
    for i in range(-1,m-1):
        if re<abs(b[i]-b[i+1]):
            re=abs(b[i]-b[i+1])
    return re
    
    
for i in range(n):
    m=int(input())
    a=list(map(int,input().split()))
    a.sort()
    print(find(a,m))
