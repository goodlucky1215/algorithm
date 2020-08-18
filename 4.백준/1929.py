M,N=map(int,input().split())
sosu=[True]*(N+1)
sosu[1]=False
n=int(N**0.5)
if M%2==0:
    p=M
else:
    p=M-1
for i in range(2,n+1):
    if sosu[i]==True:
        for j in range(i+i,N+1,i):
            sosu[j]=False
            
for i in range(M,N+1):
    if sosu[i]==True:
        print(i)
