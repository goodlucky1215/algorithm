A=int(input())
n=0
while n!=A:
    if A%2==1:
        print('* '*(A//2+1))
        print(' *'*(A//2))
    else:
        print('* '*(A//2))
        print(' *'*(A//2))
    n+=1
