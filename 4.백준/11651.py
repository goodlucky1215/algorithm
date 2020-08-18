n=int(input())
x=[]
for i in range(n):
    x.append([])
    x[i]=list(map(int,input().split()))
x.sort(key=lambda x:(x[1],x[0]))
for i in range(n):
    print(x[i][0],x[i][1])

n=int(input())
x=[]
for i in range(n):
    x.append([])
    x[i]=list(map(int,input().split()))
    x[i][0],x[i][1]=x[i][1],x[i][0]
x.sort()
for i in range(n):
    x[i][0],x[i][1]=x[i][1],x[i][0]
    print(x[i][0],x[i][1])
