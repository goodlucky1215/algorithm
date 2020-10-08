n=int(input())
pan=[]
pan1=[]
for i in range(n):
    pan.append(list(map(int,input().split())))
    pan1.append([])
    pan1[i]=[0]*n
pan1[0][0]=1
for i in range(n):
    for j in range(n):
        k=pan[i][j]
        if k!=0:
            if 0<=k+i<n:
                pan1[k+i][j]+=pan1[i][j]
            if 0<=k+j<n:
                pan1[i][k+j]+=pan1[i][j]
print(pan1[-1][-1])
