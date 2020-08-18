import sys
M=input().split('.')

for i in range(len(M)):
    if len(M[i])%2==1:
        print(-1)
        sys.exit()
    else:
        a=len(M[i])//4
        b=len(M[i])%4
        M[i]='AAAA'*a+'B'*b

for i in range(len(M)):
    if i+1==len(M):
        print(M[i])
    else:
        print(M[i]+'.',end='')
#print('.'.join(M))        
