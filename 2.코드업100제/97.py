m=[]
for i in range(20) :
    m.append([])
    for j in range(20) :
        m[i].append(0)

n=int(input())

x=input().split()
y=input().split()

for i in range(n) :
    for j in range(20):
        m[int(j)][int(y[i])]=1
        m[int(j)][int(x[i])]=1
        m[int(x[i])][int(j)]=1
        m[int(y[i])][int(j)]=1   
for i in range(1, 20) :
        for j in range(1, 20) :
            print(m[i][j], end=' ')
        print()

print(" ")

m=[]
for i in range(20) :
    m.append([])
    for j in range(20) :
        m[i].append(0)

for i in range(n) :
        m[int(x[i])][int(x[i])]=1
        m[int(x[i])][int(y[i])]=1
        m[int(y[i])][int(y[i])]=1
        m[int(y[i])][int(x[i])]=1

for i in range(1, 20) :
        for j in range(1, 20) :
            print(m[i][j], end=' ')
        print()
