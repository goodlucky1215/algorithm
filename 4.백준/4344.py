a=int(input())
for i in range(a):
    b=list(map(int,input().split()))
    c=(sum(b)-b[0])/b[0]
    d=0
    for i in range(b[0]):
        if b[i+1]>c:
            d+=1
    print('%.3f%%' % (d/b[0]*100))