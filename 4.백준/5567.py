n=int(input())
m=int(input())
p={}
for i in range(n):
    p[i+1]=[]
for i in range(m):
    x,y=map(int,input().split())
    p[x].append(y)
    p[y].append(x)
s=set()
s.update(p[1])
for i in p[1]:
    s.update(p[i])
print(len(s)-1)
