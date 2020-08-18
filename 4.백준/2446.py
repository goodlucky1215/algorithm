A=int(input())
for i in range(1,A+1):
    print(' '*(i-1)+'*'*(1+2*(A-i)))
for i in range(1,A):
    print(' '*(A-i-1)+'*'*(1+2*(i)))
