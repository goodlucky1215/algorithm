n,m=map(int,input().split())
num=list(map(int,input().split()))
for i in range(m):
    num.sort()
    k=num[0]+num[1]
    num[0],num[1]=k,k
print(sum(num))
