import sys
from itertools import permutations
n=int(input())
num=list(sys.stdin.readline().split())
a=list(map(int,sys.stdin.readline().split()))
b=[]
b+=['+']*a[0]+['-']*a[1]+['*']*a[2]+['//']*a[3]
b1=list(permutations(b,n-1))
b1=list(set(b1))
ma=0
mi=0
s=''
ma=-1e9
mi=1e9
for j in range(len(b1)):
    s=''
    s+=num[0]
    for i in range(n-1):
        if b1[j][i]=='//' and int(s)<0 and int(num[i+1])>0:
            s=(-int(s))//int(num[i+1])
            s='-'+str(s)
        else:
            s+=b1[j][i]
            s+=num[i+1]
            s=str(eval(s))
    s=int(s)
    ma=max(ma,s)
    mi=min(mi,s)
print(ma)
print(mi)

ma=-1e9
mi=1e9
m=int(input())
num=list(map(int,input().split()))
a1,a2,a3,a4=map(int,sys.stdin.readline().split())
def find(n,i,a1,a2,a3,a4):
    global ma,mi
    if i==m:
        ma=max(ma,n)
        mi=min(mi,n)
    else:
        if a1:find(n+num[i],i+1,a1-1,a2,a3,a4)
        if a2:find(n-num[i],i+1,a1,a2-1,a3,a4)
        if a3:find(n*num[i],i+1,a1,a2,a3-1,a4)
        if a4:find(int(n/num[i]),i+1,a1,a2,a3,a4-1)
find(num[0],1,a1,a2,a3,a4)
print(ma)
print(mi)
