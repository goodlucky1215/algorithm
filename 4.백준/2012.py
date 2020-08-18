N=int(input())
k=[]
n=0
for i in range(N):
    k.append(int(input()))
k.sort()
for i in range(1,N+1):
    n+=abs(k[i-1]-i)
print(n)
