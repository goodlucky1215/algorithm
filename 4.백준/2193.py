n=int(input())
a=1
b=1
#이건 규칙이 있는 문제로 점화식으로 풀면된
if n==1 or n==2:
    print(1)
else:
    for i in range(n-2):
        re=a+b
        a,b=b,re
    print(re)
    
