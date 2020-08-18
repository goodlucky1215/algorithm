a=list(range(1,10001))
b=list(range(1,10001))
for i in range(len(a)):
    k=a[i]
    for j in str(k):
            k+=int(j)
    if k in b:
            b.remove(k)
for i in b:
    print(i)