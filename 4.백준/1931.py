N=int(input())
b=[]
z=100000000000
for i in range(N):
    b.append(list(map(int,input().split()))[::-1])

b=sorted(b)

c=1
z=b[0][0]

for i in range(1,N):
    if z<=b[i][1]:
        z=b[i][0]
        c+=1

        
print(c)
