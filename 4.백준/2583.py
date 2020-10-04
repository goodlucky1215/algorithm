def find(i,j,a):
    k=1
    p=[[i,j]]
    x=[0,1,-1,0]
    y=[1,0,0,-1]
    while p:
        i,j=p.pop(0)
        for i1 in range(4):
            if 0<=i-x[i1]<m and 0<=j-y[i1]<n and a[i-x[i1]][j-y[i1]]==0:
                k+=1
                a[i-x[i1]][j-y[i1]]=1
                p.append([i-x[i1],j-y[i1]])
    return k
        
m,n,k=map(int,input().split())
a=[]
for i in range(m):
    a.append([])
    a[i]=[0]*n
for i in range(k):
    x1,y1,x2,y2=map(int,input().split())
    for j in range(x1,x2):
        for k in range(y1,y2):
            a[k][j]=1
re=0
p=[]
for i in range(m):
    for j in range(n):
        if a[i][j]==0:
            re+=1
            a[i][j]=1
            p.append(find(i,j,a))
print(re)
p.sort()
print(*p)
