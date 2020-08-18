a,b,c=map(int,input().split())
d=0
for i in range(a):
    for k in range(b):
        for f in range(c):
            print(i,k,f)
            d+=1

print(d)
