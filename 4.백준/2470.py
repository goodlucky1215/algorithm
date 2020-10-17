n=int(input())
s=list(map(int,input().split()))
s.sort()
st=0
end=n-1
ans=2000000000
while st<end:
    n=s[st]+s[end]
    if abs(n)<abs(ans):
        ans=n
        a=s[st]
        b=s[end]
    if n>0:
        end-=1
    elif n<0:
        st+=1
    else:
        break
print(a,b)
    
    


import sys
n=int(input())
s=list(map(int,input().split()))
a1=[]
a2=[]
for i in s:
    if i>=0:
        a1.append(i)
    else:
        a2.append(i)
a1.sort() #플러스값
a2.sort() #마이너스값
if a1==[]:
    print(a2[-2],a2[-1])
elif a2==[]:
    print(*a1[:2])
else:
    re=[10**9,10**9]
    k=len(a2)
    if k>=2:
        re=[a2[-2],a2[-1]]
    if len(a1)>=2:
        if abs(sum(re))>abs(sum(a1[:2])):
            re=a1[:2]
    for i in a1:
        st=0
        end=k-1
        while st<=end:
            mid=(st+end)//2
            if i+a2[mid]==0:
                print(a2[mid],i)
                sys.exit()
            else:
                if abs(sum(re))>abs(i+a2[mid]):
                    re=[a2[mid],i]
            if i+a2[mid]>0:
                end=mid-1
            elif i+a2[mid]<0:
                st=mid+1
    print(*re)
            
            
