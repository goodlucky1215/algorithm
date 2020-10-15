k1=0
def find(n,s,e,l):
    global k1
    if s>e:
        return
    mid=(s+e)//2
    re=0
    if mid==0:
        return
    for i in l:
        re+=i//mid
    if n<=re:
        k1=max(k1,mid)
        return find(n,mid+1,e,l)
    else:
        return find(n,s,mid-1,l)
k,n=map(int,input().split())
l=[]
total=0
for i in range(k):
    a=int(input())
    l.append(a)
    total+=a
total//=n
if total==0:
    print(0)
elif total==1:
    print(1)
else:
    find(n,0,total,l)
    print(k1)
