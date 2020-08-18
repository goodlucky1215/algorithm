import sys
T=int(sys.stdin.readline())
for i in range(T):
    x,y=map(int,sys.stdin.readline().split())
    re=y-x
    n=p=z=1
    while re>p:  
        if n%2==0:
            z+=1
        p+=z
        n+=1
    print(n)
