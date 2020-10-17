import heapq
import sys
input=sys.stdin.readline
n,m,l=map(int,input().split())
a=[0]
a+=list(map(int,input().split()))
a.append(l)
a.sort()
b1=[]
b=[]
for i in range(n+1):
    b1.append(a[i+1]-a[i])
    heapq.heappush(b,[-(a[i+1]-a[i]),i,1])
for i in range(m):
        k=heapq.heappop(b)
        k[2]+=1
        k1=b1[k[1]]//k[2]
        if b1[k[1]]%k[2]>0:
            k1+=1
        heapq.heappush(b,[-k1,k[1],k[2]])
re=heapq.heappop(b)
print(-re[0])
