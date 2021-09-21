import heapq
import sys
input=sys.stdin.readline
n=int(input())
a=[]
b=[]
for i in range(n):
    b1,b2=map(int,input().split())
    heapq.heappush(a,[b2,b1])
    b.append([b1,b2])
b.sort()
re=0
for i in b:
    re+=1
    b1=i[:]
    a1=[]
    p=len(a)
    print(i,a)
    for j in range(p):
        k=heapq.heappop(a)
        k1=[k[0],k[1]]
        if i!=k1:
            if k[0]<b1[1]:
                    heapq.heappush(a1,k)
            else:
                b1=k
    a=[]
    heapq.heappush(a,a1)
    if a==[]:
        break
print(re)

s=heapq.heappop(a)
p=[s]
re=1
for i in range(n-1):
    k=heapq.heappop(a)
    t=True
    for j in range(re):
        if k[1]>=p[j][0]:
            p[j]=k
            t=False
            break
    if t:
        re+=1
        p.append(k)

print(re)
