def find(k,b1):
    re=0
    n1=[1,0,0,-1]
    m1=[0,-1,1,0]
    while b1:
        i=b1.pop(0)
        print(i)
        for j in range(4):
            if 0<=i[0]+n1[j]<n and 0<=i[1]+m1[j]<m and k[i[0]+n1[j]][i[1]+m1[j]]==0:
                k[i[0]+n1[j]][i[1]+m1[j]]=2
                b1.append([i[0]+n1[j],i[1]+m1[j]])
    for i in range(n):
        re+=k[i].count(0)
    
    return re

from itertools import combinations
import copy
n,m=map(int,input().split())
p=[]
a=[]
b=[]
for i in range(n):
    p.append(list(map(int,input().split())))
    for j in range(m):
        if p[i][j]==0:
            a.append([i,j])
        if p[i][j]==2:
            b.append([i,j])
a=list(combinations(a,3))
f=0
for i in a:
    b1=b[:]
    k=copy.deepcopy(p)
    for j in i:
        k[j[0]][j[1]]=1
    f=max(f,find(k,b1))
print(f)
