import sys
n=int(input())
p=[]
for i in range(n):
    p.append(list(map(int,sys.stdin.readline().split())))
a=[p[0][0]]
for i in range(1,n):
    for j in range(len(p[i])):
        if j==0:
            p[i][0]+=p[i-1][0]
        elif j==len(p[i])-1:
            p[i][j]+=p[i-1][i-1]
        else:
            p[i][j]+=max(p[i-1][j-1],p[i-1][j])
print(max(p[n-1]))
        
        
    
