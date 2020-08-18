N,M,K= map(int,input().split())
while K:
    if N >= 2*M:
        N -=1
    else:
        M -=1
    K -= 1

print(min(N//2,M))