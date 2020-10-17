import heapq
import sys
n=int(sys.stdin.readline())
num=[]
for i in range(n):
    a=int(sys.stdin.readline())
    if a==0:
        if num:
            k=-heapq.heappop(num)
            print(k)
        else:
            print(0)
    else:
        heapq.heappush(num,-a)
