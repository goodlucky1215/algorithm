n=int(input())
po=[0]
for i in range(n):
    po.append(int(input()))
if n==1:
    k=[0,po[1]]
elif n>=2:
    k=[0,po[1],po[1]+po[2]]
for i in range(3,n+1):
    k.append(max(po[i]+po[i-1]+k[i-3],po[i]+k[i-2],k[i-1]))
print(k[-1])
