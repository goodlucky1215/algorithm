n=int(input())
a=[]
b={}
for i in range(n):
    a.append(input())
    for j in range(len(a[i])):
        if a[i][j] not in b:
            #크기의 중요성을 10의제곱으로 표
            b[a[i][j]]=10**(len(a[i])-1-j)
        else:
            b[a[i][j]]+=10**(len(a[i])-1-j)
b=list(sorted(b,key=lambda x:b[x],reverse=True))
k=9
c={}
for i in b:
    c[i]=str(k)
    k-=1
for i in  range(n):
    for j in a[i]:
        a[i]=a[i].replace(j,c[j])
re=0
for i in a:
    re+=int(i)
print(re)
    
    
