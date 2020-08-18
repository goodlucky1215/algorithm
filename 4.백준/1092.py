import sys
n = int(sys.stdin.readline())
c= list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b= list(map(int, sys.stdin.readline().split()))

c.sort(reverse=True)
b.sort(reverse=True)

if c[0]<b[0]:
    print(-1)
    sys.exit()

c1=[0]*n
b1=[False]*m
result=0
count=0

while True:
    if count==len(b):
        break
    for i in range(n):
        while c1[i]<len(b):
            if b1[c1[i]]==False and c[i]>=b[c1[i]]:
                b1[c1[i]]=True
                c1[i]+=1
                count+=1
                break
            c1[i]+=1
    result+=1

print(result)
