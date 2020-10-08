import sys
sys.setrecursionlimit(1000000000)
di=[0,0,-1,1]
dj=[-1,1,0,0]
def dfs1(i,j):
    b[i][j]=True
    for q in range(4):
        t_i=i+di[q]
        t_j=j+dj[q]
        if 0<= t_i <= n-1 and 0<= t_j <= n-1 and not(b[t_i][t_j]):
            if a[i][j]==a[t_i][t_j]:
                b[t_i][t_j]=True
                dfs1(t_i,t_j)
            
def dfs2(i,j):
    b[i][j]=False
    for q in range(4):
        t_i=i+di[q]
        t_j=j+dj[q]
        if 0<= t_i <= n-1 and 0<= t_j <= n-1 and (b[t_i][t_j]):
            if a[i][j]=='R' or a[i][j]=='G':
                if 'R'==a[t_i][t_j] or 'G'==a[t_i][t_j]:
                    b[t_i][t_j]=False
                    dfs2(t_i,t_j)
            else:
                if a[i][j]==a[t_i][t_j]:
                    b[t_i][t_j]=False
                    dfs2(t_i,t_j)

n=int(input())
a=[]
P1,P2=0,0
b=[]
for i in range(n):
    a.append(input())
    b.append([])
    b[i]=[False]*n
for i in range(n):
    for j in range(n):
        if not b[i][j]:
            dfs1(i,j)
            P1+=1
for i in range(n):
    for j in range(n):
        if b[i][j]:
            dfs2(i,j)
            P2+=1
print(P1,P2)
