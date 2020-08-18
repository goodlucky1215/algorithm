import sys
N=list(map(int,sys.stdin.readline().split()))
N.remove(max(N))
print(max(N))
