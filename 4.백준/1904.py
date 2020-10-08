a=int(input())
b=[0]*1000001
b[1]=1
b[2]=2
for i in range(3,a+1):
    b[i]=(b[i-2]+b[i-1])%15746
print(b[a])
