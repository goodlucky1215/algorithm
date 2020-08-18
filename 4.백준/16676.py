N=int(input())
a=len(str(N))-1
b=1
while a != 0:
    b+=10**a
    a-=1
if N==0:
    print(1)
elif N>=b:
    print(len(str(N)))
else:
    print(len(str(N))-1)


N=input()
S='1'*len(N)

if int(N)==0:
    print(1)
elif int(N) >= int(S):
        print(len(N))
else:
        print(len(N)-1)
