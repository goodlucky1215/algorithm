n,m=map(int,input().split())
t=[]
re=0
for i in range(n):
    t.append(list(map(int,input().split())))

#1번블럭
for i in range(n):
    for j in range(m-3):
        p=0
        for k in range(4):
            p+=t[i][k+j]
        re=max(re,p)
for i in range(m):
    for j in range(n-3):
        p=0
        for k in range(4):
            p+=t[j+k][i]
        re=max(re,p)
#2번블럭
for i in range(n-1):
    for j in range(m-1):
        p=0
        p+=t[i][j]+t[i+1][j]+t[i][j+1]+t[i+1][j+1]
        re=max(re,p)
#3번과 5번 블럭
for i in range(n-1):
    for j in range(m-2):
        p=0
        s=0
        p=max(t[i+1][j],t[i+1][j+1],t[i+1][j+2])
        s=max(t[i][j],t[i][j+1],t[i][j+2])
        for k in range(3):
            p+=t[i][j+k]
            s+=t[i+1][j+k]
        re=max(re,p,s)
for i in range(m-1):
    for j in range(n-2):
        p=0
        s=0
        p=max(t[j][i+1],t[j+1][i+1],t[j+2][i+1])
        s=max(t[j][i],t[j+1][i],t[j+2][i])
        for k in range(3):
            p+=t[j+k][i]
            s+=t[j+k][i+1]
        re=max(re,p,s)
#4번블록
for i in range(n-1):
    for j in range(m-2):
        p=0
        p=max(t[i][j]+t[i+1][j+2],t[i+1][j]+t[i][j+2])
        p+=t[i][j+1]+t[i+1][j+1]
        re=max(re,p)
for i in range(m-1):
    for j in range(n-2):
        p=0
        p=max(t[j][i]+t[j+2][i+1],t[j][i+1]+t[j+2][i])
        p+=t[j+1][i]+t[j+1][i+1]
        re=max(re,p)
print(re)
    

    
