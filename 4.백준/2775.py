T=int(input())
for i in range(T):
    k=int(input())
    n=int(input())
    number=list(range(1,n+1))
    for f in range(k):
        for j in range(1,n):
            number[j]=sum(number[j-1:j+1])
    print(number[-1])
