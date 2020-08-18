x=int(input())
a=b=99
if x<=99:
    print(x)
else:
    while a<x:
        a+=1
        if int(str(a)[0])-int(str(a)[1])==int(str(a)[1])-int(str(a)[2]):
            b+=1
    print(b)
