m=[]
for i in range(19):
    m.append([])
    for j in range(19):
        m[i].append(0)


a=int(input())

for i in range(a):
    x, y= map(int,input().split())
    m[x-1][y-1]=1

for i in range(19):
    for j in range(19):
        print(m[i][j], end=" ")
    print(" ")
    
