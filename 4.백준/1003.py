n=int(input())
a=[[1,0],[0,1],[1,1]]
for i in range(n):
    b=int(input())
    if len(a)>=b+1:
        print(*a[b])
    else:
        k=len(a)
        for j in range(b-k+1):
            a.append([])
            a[-1].append(a[-2][1])
            a[-1].append(a[-2][1]+a[-3][1])
        print(*a[b])
