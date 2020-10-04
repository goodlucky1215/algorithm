n=int(input())
a=[]
b=[]
for i in range(n):
    a.append(list(map(int,input().split())))
    b.append([])
    b[i]=[0]*3
b[0]=a[0]
for i in range(1,n):
    b[i][0]=min(b[i-1][1]+a[i][0],b[i-1][2]+a[i][0])
    b[i][1]=min(b[i-1][0]+a[i][1],b[i-1][2]+a[i][1])
    b[i][2]=min(b[i-1][0]+a[i][2],b[i-1][1]+a[i][2])
print(min(b[n-1]))
