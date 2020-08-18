A=[]
B=[]
for i in range(3):
    a, b=map(int,input().split())
    A.append(a)
    B.append(b)
if A[0]==A[1]:
    A=A[2]
elif A[0]==A[2]:
    A=A[1]
else:
    A=A[0]
if B[0]==B[1]:
    B=B[2]
elif B[0]==B[2]:
    B=B[1]
else:
    B=B[0]
print(A,B)