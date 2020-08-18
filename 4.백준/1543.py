print(input().count(input()))

N=input()
M=input()
k=0
a=len(M)
result=0
while True:
    if len(N)>k and len(N)>=a:
        if N[k:a]==M:
            result+=1
            k=a
            a+=len(M)
        else:
            k+=1
            a+=1
    else:
        break
print(result)
