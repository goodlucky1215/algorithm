def find(tree,s,e,k,n):
    if s>e:
        print(k)
        return
    mid=(s+e)//2
    re=0
    for i in range(n):
        if mid<tree[i]:
            re+=(tree[i]-mid)
    if m<=re:
        k=max(k,mid)
        find(tree,mid+1,e,k,n)
    else:
        find(tree,s,mid-1,k,n)
n,m=map(int,input().split())
tree=list(map(int,input().split()))
ma=max(tree)
k=0
find(tree,0,ma,k,n)
