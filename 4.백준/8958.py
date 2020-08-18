a=int(input())
b=0
for i in range(a):
    c=input().split('X')
    b=0
    for j in c:
        for k in range(len(j)+1):
            b+=k
    print(b)
