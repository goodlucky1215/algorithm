import sys
a,b=map(int,sys.stdin.readline().split())
N=list(map(int,sys.stdin.readline().split()))
for i in N:
    if i<b:
        print(i,end=' ')
