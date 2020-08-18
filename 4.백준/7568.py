N = int(input())
p=[]
z=[]
a=[1]*N
for i in range(N):
    x,y=map(int,input().split())
    p.append(x)
    z.append(y)
for i in range(len(p)-1):
    for j in range(i+1,len(p)):
        if p[i]>p[j] and z[i]>z[j]:
            a[j]+=1
        elif p[i]<p[j] and z[i]<z[j]:
            a[i]+=1
print(*a)
