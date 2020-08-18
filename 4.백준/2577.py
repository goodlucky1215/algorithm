A=int(input())
B=int(input())
C=int(input())
Z=str(A*B*C)
result=[0]*10
for i in Z:
    result[int(i)]+=1
for i in result:
    print(i)
