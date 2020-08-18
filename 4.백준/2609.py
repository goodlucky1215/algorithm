a,b=map(int,input().split())
ma=1
mi=1
c=2
while a!=1 or b!=1:
    if a%c==0 and b%c==0:
        ma*=c
        mi*=c
        a/=c
        b/=c
    elif a%c==0 and b%c!=0:
        mi*=c
        a/=c
    elif a%c!=0 and b%c==0:
        mi*=c
        b/=c
    else:
        c+=1
print(ma)
print(mi)
