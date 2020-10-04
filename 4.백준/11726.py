n=int(input())
a=1
b=2
re=0
if n<=2:
    print(n)
else:
    for i in range(n-2):
        re=(a+b)%10007
        a=b
        b=re
    print(re)
