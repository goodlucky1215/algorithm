import sys
n,m=map(int,input().split())
se=[]
farm=[]
for i in range(m):
    farm.append(list(map(int,sys.stdin.readline().split())))
    for j in range(n):
        if farm[i][j]==1:
            se.append([i,j])
x=[0,0,1,-1]
y=[1,-1,0,0]
count=0
while se:
    count+=1
    p=[]
    for i in se:
        for j in range(4):
            x1=i[0]+x[j]
            y1=i[1]+y[j]
            if 0<=x1<m and 0<=y1<n and farm[x1][y1]==0:
                farm[x1][y1]=1
                p.append([x1,y1])
    se=p[:]
for i in range(m):
    if 0 in farm[i]:
        print(-1)
        sys.exit()
print(count-1)
    
