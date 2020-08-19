n=int(input())

def find(k,a):
    for i in range(2,k+1):
        for j in range(i,k+1,i):
            if not a[j]:
                a[j]=True
            else:
                a[j]=False
    return print(a.count(False)-1)
for i in range(n):
    k=int(input())
    a=[False]*(k+1)
    find(k,a)
