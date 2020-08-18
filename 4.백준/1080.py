N, M =map(int,input().split())

A=[list(map(int,list(input()))) for i in range(N)]
B=[list(map(int,list(input()))) for i in range(N)]

n=0

def chage(i,j):
    for k in range(i,i+3):
        for h in range(j,j+3):
            if A[k][h]==0:
                A[k][h]=1
            else:
                A[k][h]=0
                
for i in range(N-2):
    for j in range(M-2):
        if A[i][j]!=B[i][j]:
            n+=1
            chage(i,j)
            
def check():            
    for i in range(N):
        for j in range(M):
            if A[i][j]!=B[i][j]:
                    return print(-1)
                    break
    return print(n)

check()
