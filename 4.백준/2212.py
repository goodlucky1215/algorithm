n=int(input())
k=int(input())
sencer=sorted(list(map(int, input().split())))

s=[]
for i in range(0,n-1):
    s.append(sencer[i+1]-sencer[i])
s.sort(reverse=True)
print(sum(s[k-1:]))
