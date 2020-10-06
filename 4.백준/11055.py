n=int(input())
num=list(map(int,input().split()))
count=0
ma=[0]*n
ma[0]=num[0]
for i in range(n):
    ma[i]=num[i]
    for j in range(i):
        if num[i]>num[j] and num[i]+ma[j]>ma[i]:
            ma[i]=num[i]+ma[j]
    if count<ma[i]:
        count=ma[i]
print(count)
