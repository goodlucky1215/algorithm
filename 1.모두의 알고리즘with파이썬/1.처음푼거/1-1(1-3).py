def gub(n):
    s=0
    for i in range(n):
        s=s+i**2
    return s

print(gub(10))

def gub1(n):
    return n*(n+1)(2*n+1)//6

print(gub1(10))
