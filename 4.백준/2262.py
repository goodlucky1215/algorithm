n=int(input())
num=list(map(int,input().split()))
result=0
while 1 != len(num):
    a = num.index(max(num))
    if a+1 >= len(num):
        result+=(num[a]-num[a-1])
        num.pop(a)
    elif a == 0:
        result+=(num[a]-num[a+1])
        num.pop(a)
    else:
        if num[a+1]>num[a-1]:
            result+=(num[a]-num[a+1])
            num.pop(a)
        else:
            result+=(num[a]-num[a-1])
            num.pop(a)

print(result)
