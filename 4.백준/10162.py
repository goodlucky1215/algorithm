t=int(input())
a=[0,0,0]
if t>=300:
    a[0]+=t//300
    t-=a[0]*300
if t>=60:
    a[1]+=t//60
    t-=a[1]*60
if t>=10:
    a[2]+=t//10
    t-=a[2]*10
if t==0:
    print(*a)
else:
    print(-1)
