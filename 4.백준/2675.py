import sys
a=int(input())
for i in range(a):
    b,c=sys.stdin.readline().split()
    for j in c:
        print(j*int(b),end='')
    print()
