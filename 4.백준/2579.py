import sys
n=int(input())
if n==0:
    print(0)
    sys.exit()
d=[0]
for i in range(n):
    d.append(int(input()))
p=[0,d[1]]
if n>1:
    p.append(d[1]+d[2])
if n>=2:
    for i in range(3,n+1):
        p.append(max(d[i]+d[i-1]+p[i-3],d[i]+p[i-2]))
print(p[n])
