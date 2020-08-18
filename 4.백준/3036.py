N=int(input())
M=list(map(int,input().split()))
for i in M[1:]:
    n=2
    a=M[0]
    b=i
    if a%b==0:
        print('%d/1' %(a/b))
    else:
        while n<i:
            if a%n==0 and b%n==0:
                a//=n
                b//=n
            else:
                n+=1
        print('%d/%d' %(a,b))
            
