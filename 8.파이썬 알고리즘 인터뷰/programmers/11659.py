import sys
input=sys.stdin.readline
'oxoxoxoxox'.index('x',1, 2)
n, m = map(int,input().split())
su = list(map(int,input().split()))
for index in range(1,n):
    su[index]+=su[index-1]
for i in range(m):
    a,b = map(int,input().split())
    a-=2
    if a>=0:
        print(su[b-1]-su[a])
    else:
        print(su[b-1])