a=int(input())
b=d=res=0
c=1
if a==0:
    print(d)
elif a==1:
    print(1)
else:
    while d!=a-1:
         res=b+c
         d+=1
         b=c
         c=res
    print(res)
