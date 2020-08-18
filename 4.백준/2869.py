A,B,V = map(int,input().split())
V=V-A
A=A-B
if V%A !=0:
    print(V//A+2)
else:
    print(V//A+1)