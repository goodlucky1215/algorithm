N=int(input())
n=list(map(int,input().split()))
z=[i+1 for i in range(N)]
for i in range(N-1):
        d=n[-i-2]+N-2-i
        p=z.pop(-i-2)
        z.insert(d,p)

for i in z:
    print(i,end=' ')
