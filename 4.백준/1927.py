import heapq
import sys
n=int(sys.stdin.readline())
num=[]
for i in range(n):
    a=int(sys.stdin.readline())
    if a==0:
        if num:
            print(heapq.heappop(num))
        else:
            print(0)
    else:
        heapq.heappush(num,a)
