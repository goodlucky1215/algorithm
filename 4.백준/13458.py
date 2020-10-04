n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
re=len(a)
for i in a:
    d=i-b
    if d>0:
        re+=d//c
        if 0!=d%c:
            re+=1
print(re)
