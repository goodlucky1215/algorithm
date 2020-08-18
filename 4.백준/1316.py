a=int(input())
b=0
for i in range(a):
    b+=1
    c=input()
    d=[]
    for j in c:
        if j not in d:
            d.append(j)
        elif j in d and j!=d[-1]:
            b-=1
            break
print(b)
