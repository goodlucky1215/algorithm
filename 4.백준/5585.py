N=int(input())
N=1000-N
c=0
b=[500,100,50,10,5,1]
for i in b:
    c+=N//i
    N %= i

print(c)
