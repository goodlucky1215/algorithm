import heapq
import sys
n=int(sys.stdin.readline())
num=[]
num1=[]
for i in range(n):
    a=int(sys.stdin.readline())
    if a==0:
        if num:
            k=heapq.heappop(num)
            if k[1]==1:
                print(k[0])
            else:
                print(-k[0])
        else:
            print(0)
    else:
        if a>0:
            heapq.heappush(num,[a,1])
        else:
            heapq.heappush(num,[-a,0])
