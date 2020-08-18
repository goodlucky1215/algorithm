x=list(map(int,input()))
x.sort(reverse=True)

if x[-1]==0 and sum(x)%3==0:
        for i in x:
            print(i,end='')
        
else:
    print(-1)
