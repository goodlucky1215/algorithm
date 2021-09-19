n=int(input())
n1=list(range(n+1))
m=int(input())
b=[0]
per=[]
for i in range(m):
    b.append(int(input()))
    per.append([])
    per[-1]=n1[b[i]+1:b[i+1]]
    if not per[-1]:
        per.pop()
per.append([])
per[-1]=n1[b[m]+1:]
if not per[-1]:
        per.pop()
re=1
a=[1,2,3]
for i in per:
    if len(i)<=len(a):
        re*=a[len(i)-1]
    else:
        for j in range(len(i)-len(a)):
            a.append(a[-1]+a[-2])
        re*=a[-1]
print(re)    
