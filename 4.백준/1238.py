import sys
n,m,z=map(int, sys.stdin.readline().split())
a=[[m * 100 for _ in range(n)] for _ in range(n)]
for i in range(m):
    x,y,t=map(int, sys.stdin.readline().split())
    a[x-1][y-1]=t
re=[]
for k in range(n):
    for i in range(n):
        if a[i][k]!=m * 100:
            for j in range(n):
                if i==j:
                    a[i][j]=0
                else:
                    a[i][j]=min(a[i][j],a[i][k]+a[k][j])
p=0       
for i in range(n):
    p=max(p,a[i][z-1]+a[z-1][i])
print(p)
