#이분탐색으로 푸는법
import sys
def find(a,x,start,end):
    if start>end:
        return 0
    mid=(start+end)//2
    if x==a[mid]:
        return 1
    elif x>a[mid]:
        return find(a,x,mid+1,end)
    else:
        return find(a,x,start,mid-1)
t=int(sys.stdin.readline())
for i in range(t):
    n=int(sys.stdin.readline())
    me1=list(map(int,sys.stdin.readline().split()))
    me1.sort()
    m=int(sys.stdin.readline())
    me2=list(map(int,sys.stdin.readline().split()))
    for j in me2:
        print(find(me1,j,0,n-1))
        
#그냥 푸는 법
import sys
t=int(sys.stdin.readline())
for i in range(t):
    n=int(sys.stdin.readline())
    me1=set(map(int,sys.stdin.readline().split()))
    m=int(sys.stdin.readline())
    me2=list(map(int,sys.stdin.readline().split()))
    for i in me2:
        if i in me1:
            print(1)
        else:
            print(0)
        
