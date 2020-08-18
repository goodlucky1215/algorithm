a=int(input())
for i in range(a):
    H,W,N=map(int,input().split())
    b = N//H
    c = N%H
    if c!=0:
        b+=1
        print('%d%.2d'%(c,b))
    else:
        print('%d%.2d'%(H,b))
