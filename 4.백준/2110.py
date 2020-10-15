k=0
def find(m,s,e,wi,n):
    global k
    if s>e:
        return
    mid=(s+e)//2
    re=wi[0]
    re1=1
    for i in range(1,n):
        if wi[i]>=mid+re:
            re1+=1
            re=wi[i]
    if re1>=m:
        k=max(k,mid)
        return find(m,mid+1,e,wi,n)
    else:
        return find(m,s,mid-1,wi,n)

n,m=map(int,input().split())
wi=[]
for i in range(n):
    wi.append(int(input()))
wi.sort()
find(m,1,wi[-1]-wi[0],wi,n)
print(k)
