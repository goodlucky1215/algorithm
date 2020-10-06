n=int(input())
s=[]
for i in range(n):
    s.append(int(input()))
k=[1]*n
count=0
for i in range(n):
    for j in range(i):
        if s[i]>s[j] and k[j]+1>k[i]:
            k[i]=k[j]+1
    if count<k[i]:
        count=k[i]
print(n-count)
        
