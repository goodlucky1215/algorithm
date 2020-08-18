a=123456*2
sosu=[True]*(a+1)
sosu[0]=sosu[1]=False
p=int(a**0.5)
for i in range(2,p+1):
    for j in range(i+i,a+1,i):
        sosu[j]=False

while True:
    N=int(input())
    d=0
    if N==0:
        break
    P=N*2
    for i in range(N+1,P+1):
        if sosu[i]==True:
            d+=1
    print(d)