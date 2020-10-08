t=[]
for i in range(4):
    t.append(list(input()))
def find(m,n):
    global t
    to=[0,0,0,0]
    to[m-1]=n
    k=m-1
    while k>0:
        if t[k][6]!=t[k-1][2]:
            to[k-1]=-to[k]
        else:
            break
        k-=1
    k=m-1
    while k<3:
        if t[k][2]!=t[k+1][6]:
            to[k+1]=-to[k]
        else:
            break
        k+=1
    for i in range(4):
        if to[i]==1:
            k=t[i].pop()
            t[i].insert(0,k)
        elif to[i]==-1:
            k=t[i].pop(0)
            t[i].append(k)
re=0    
for i in range(int(input())):
    m,n=map(int,input().split())
    find(m,n)
for i in range(4):
    if t[i][0]=='1':
        re+=2**i
print(re)
