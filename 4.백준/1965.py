n=int(input())
box=list(map(int,input().split()))
count=0
ma=[0]*n
for i in range(n):
    ma[i]=1
    for j in range(i):
        if box[i]>box[j] and ma[j]+1>ma[i]:
            ma[i]=ma[j]+1
    if count<ma[i]:
        count=ma[i]
print(count)
