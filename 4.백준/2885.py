N=int(input())
a=1
d=0
while a<N:
    a=a<<1
c=a
while N>0:   
    if N>=c:
        N-=c
    else:
        c//=2
        d+=1
        
print(a,d)
    
