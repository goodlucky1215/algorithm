N, M=map(int,input().split())
b=[]
result=''
dnasum=0
for i in range(N):
    b.append(input())

def DNA(a):
    global result
    if a==0:
        result+='A'
    elif a==1:
        result+='C'
    elif a==2:
        result+='G'
    else:
        result+='T'

for i in range(M):
    a=[0,0,0,0] #a,c,g,t
    for k in range(N):
        if b[k][i]=='A':
            a[0]+=1
        elif b[k][i]=='C':
            a[1]+=1
        elif b[k][i]=='G':
            a[2]+=1
        else:
            a[3]+=1
    DNA(a.index(max(a)))
    dnasum+=(N-max(a))


        
print(result)
print(dnasum)
