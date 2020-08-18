A=int(input())
n=[]
for i in range(A):
    p=int(input())
    if p!=0:
        n.append(p)
    elif p==0:
        n.pop()
print(sum(n))
        
