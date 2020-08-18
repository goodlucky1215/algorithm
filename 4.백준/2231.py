N=int(input())
a=list(range(N))
a=a[N//2:]
p=[]
for i in a:
    b=i
    for j in str(i):
        b+=int(j)
    if b==N:
        p.append(int(i))
if bool(p)==False:
    print(0)
else:
    print(min(p))
