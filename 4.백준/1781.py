N=int(input())
cup=[]
result=[]
for i in range(N):
    cup.append(list(map(int,(list(input().split())))))
cup.sort()
for i in cup:
    if len(result)<i[0]:
        result.append(i[1])
    else:
        if min(result)<i[1]:
            result[result.index(min(result))]=i[1]
print(sum(result))
