a=int(input())
b=c=1
d=0
if a==1 or a==2:
    d=1
else:    
    for i in range(a-2):
        d=b+c
        b=c
        c=d
print(d)
