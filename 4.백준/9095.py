n=int(input())
pi=[1,2,4]
for i in range(n):
    a=int(input())
    if len(pi)>a:
        print(pi[a-1])
    else:
        k=len(pi)
        for j in range(a-k):
            pi.append(pi[-1]+pi[-2]+pi[-3])
        print(pi[a-1])
