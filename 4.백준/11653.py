n=int(input())
p=2
while n>=p:
        if n%p==0:
               n=n/p
               print(p)
        else:
               p+=1
