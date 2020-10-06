import sys
n=int(input())
num=list(map(int,sys.stdin.readline().split()))
re=num[0]
for i in range(1,n):
    if num[i-1]+num[i]>num[i]:
        num[i]+=num[i-1]
    re=max(re,num[i])
print(re)
            
