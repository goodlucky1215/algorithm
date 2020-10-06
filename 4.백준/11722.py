import sys
n=int(sys.stdin.readline())
num=list(map(int,sys.stdin.readline().split()))
count=0
mi=[1]*n
for i in range(n):
    for j in range(i):
        if num[i]<num[j] and mi[j]+1>mi[i]:
            mi[i]=mi[j]+1
    if count<mi[i]:
        count=mi[i]
print(count)
