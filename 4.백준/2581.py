M=int(input())
N=int(input())
p=[]
while M<=N:
    d=1
    for j in range(2,M+1):
        if M%j==0:
            d+=1
    if d==2:
        p.append(M)
    M+=1
if bool(p)==False:
    print(-1)
else:
    print(sum(p))
    print(p[0])
