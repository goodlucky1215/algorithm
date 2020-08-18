n,m=map(int,input().split())
if n==1:
    print(1)
elif n==2:
    if m<=6:
        print((m + 1)//2)
    else:
        print(4)
else:
    if m<=3:
        print(m)
    elif m>=4 and m<=6:
        print(4)
    else:
        print(m-2)



