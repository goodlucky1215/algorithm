n,m=map(int,input().split())
result=[]
subject=n
for i in range(n):
    P,L=map(int,input().split())
    mpoint=list(map(int,input().split()))
    mpoint.sort(reverse=True)
    if P<L:
        result.append(1)
    else:
        result.append(mpoint[L-1])
result.sort()
while sum(result[0:subject])>m:
    subject-=1
print(subject)
