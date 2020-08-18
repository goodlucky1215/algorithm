import sys
t=int(input())
a=[]
for i in range(t):
    a.append(int(sys.stdin.readline()))
a.sort()
for i in a:
    print(i)
