n=int(input())
a=list(map(int,input().split()))
count=0
p=[1]*n
k=[]
z=0
for i in range(n):
    k.append([])
    for j in range(i):
        if a[i]>a[j] and p[j]+1>p[i]:
            p[i]=p[j]+1
            k[i]=k[j][:]
    if count<p[i]:
        count=p[i]
        z=i
    k[i].append(a[i])
print(count)
print(*k[z])

            
