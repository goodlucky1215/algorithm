a=int(input())
b=[]
for i in range(a):
    c,d=map(int,input().split())
    b.append([c,d])
b.sort()
for i in b:
    print(*i)
