import sys
input = sys.stdin.readline

def find_su():
    n = list(map(int,input().strip()))
    n.sort(reverse=True)
    if n[-1]==0 and sum(n)%3==0:
        for i in n:
            print(i, end='')

    else:
        print(-1)

find_su()