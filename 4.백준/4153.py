while True:
    A=list(map(int,input().split()))
    A.sort()
    if A[0]==0 and A[1]==0 and A[2]==0:
        break
    elif A[0]**2+A[1]**2==A[2]**2:
        print('right')
    else:
        print('wrong')