N,M=map(int,input().split())
a=list(map(int,input().split()))
mi=[]
pl=[]
result=0
for i in a:
    if i<0:
        mi.append(-i)
    else:
        pl.append(i)

mi.sort(reverse=True)
pl.sort(reverse=True)

if len(mi) ==0:
    mi.append(0)
if len(pl) ==0:
    pl.append(0)
    
i=0
while(i<len(mi)):
    result += mi[i]*2
    i += M

i=0
while(i<len(pl)):
    result += pl[i]*2
    i += M

result -=max(mi[0],pl[0])
print(result)
