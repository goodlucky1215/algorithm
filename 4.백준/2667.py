x=[0,0,-1,1]
y=[-1,1,0,0]
def find(k,i,j):
    p=1
    z=[[i,j]]
    while z:
        z1,z2=z.pop(0)
        for s in range(4):
            if 0<=x[s]+z1<n and 0<=y[s]+z2<n:
                if a[x[s]+z1][y[s]+z2]==1:
                    a[x[s]+z1][y[s]+z2]=k
                    p+=1
                    z.append([x[s]+z1,y[s]+z2])
    return p
                
n=int(input())
a=[list(map(int,list(input()))) for _ in range(n)]
count=0
k=2
re=[]
for i in range(n):
    for j in range(n):
        if a[i][j]==1:
            count+=1
            a[i][j]=k
            re.append(find(k,i,j))
            k+=1
print(count)
re.sort()
for i in re:
    print(i)
