def pibo(n,a,b):
    a=a+b
    b=a+b
    if n==3:
        return(a)
    if n==4:
        return(b)
    return pibo(n-2,a,b)

print(pibo(7,1,1))

def pibo(n):
    if n<=1:
        return n
    return pibo(n-2) + pibo(n-1)
