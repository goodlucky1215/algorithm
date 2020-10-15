def find(i,s,e,su):
    if s>e:
        return 0
    mid=(s+e)//2
    if su[mid]==i:
        return 1
    elif su[mid]<i:
        return find(i,mid+1,e,su)
    else:
        return find(i,s,mid-1,su)
n=int(input())
n1=list(map(int,input().split()))
m=int(input())
n2=list(map(int,input().split()))
n1.sort()
k=[]
for i in n2:
    k.append(find(i,0,n-1,n1))
print(*k)
