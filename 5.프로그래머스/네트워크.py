def solution(n, computers):
    n1=[False]*n
    c=0
    for i in range(n):
        if not n1[i]:
            c+=1
            n1[i]=True
            p=[i]
            s={i}
            while p:
                k=p.pop()
                for j in range(n):
                        if k!=j and computers[k][j]==1 and not n1[j]:
                            n1[j]=True
                            p.append(j)
    return c
