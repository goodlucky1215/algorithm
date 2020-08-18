a=int(input())
b=0
while a>0:
    if a%2==0:
        b = a+b
        a -= 1
    else:
        a-=1

print(b)

a=int(input())
b=0
for i in range(1,a+1):
    if(i%2==0):
        b+=i

print(b)
