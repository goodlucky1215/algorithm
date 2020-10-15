def find(i,su,s,e):
    if s>e:
        print(0)
        return
    mid=(s+e)//2
    if su[mid]==i:
        print(1)
        return
    if i>su[mid]:    
        find(i,su,mid+1,e)
    else:
        find(i,su,s,mid-1)
    
n=int(input())
su=list(map(int,input().split()))
su.sort()
m=int(input())
su1=list(map(int,input().split()))
for i in su1:
    find(i,su,0,n-1)


def find(i,su,s,e):
    mid=(s+e)//2
    if mid==e or mid==s:
        if i==su[mid]:
            print(1)
            return
        else:
            print(0)
            return 
    if i==su[mid]:
            print(1)
            return
    if i>su[mid]:    
        find(i,su,mid,e)
    else:
        find(i,su,s,mid)
    
n=int(input())
su=list(map(int,input().split()))
su.sort()
m=int(input())
su1=list(map(int,input().split()))
for i in su1:
    find(i,su,0,n)
