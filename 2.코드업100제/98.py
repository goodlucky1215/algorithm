h,w=map(int,input().split())
n=int(input())
m=[]
for i in range(h):
    m.append([])
    for j in range(w):
        m[i].append(0)

for i in range(n):
    l, d, x, y=map(int,input().split())
    if d==0:
        for j in range(l):
            m[x-1][y+int(j)-1]=1
    else:
        for j in range(l):
            m[x+int(j)-1][y-1]=1


for i in range(h):
    for j in range(w):
        print(m[i][j], end=' ')
    print(" ")
