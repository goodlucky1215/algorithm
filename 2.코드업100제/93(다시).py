#1
a=int(input())
b=map(int,input().split())
c=[0 for i in range(23)]
n=1
for i in b:
    while i!=n:
      n+=1
    c[n-1]+=1
    n=1
    
for i in c:
    print(i, end=' ')


print(" ")

#2번
a=int(input())
b=list(map(int,input().split()))
m=[0 for i in range(23)]

for i in range(a):
    m[b[i]-1]+=1

for i in range(23):
    print(m[i],end=" ")
