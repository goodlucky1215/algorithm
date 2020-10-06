n=int(input())
le=[]
for i in range(n):
    le.append(int(input()))
count=0
for i in range(n-1,0,-1):
    p=le[i]-le[i-1]
    if p<=0:
        le[i-1]+=(p-1)
        count-=(p-1)
print(count)
