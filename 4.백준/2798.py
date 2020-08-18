N,M=map(int,input().split())
p=list(map(int,input().split()))
re2=result=100000
for i in range(N-1):
    for j in range(i+1,N-1):
        for z in range(j+1,N):
            re1=p[i]+p[j]+p[z]
            if M-re1>=0 and M-re1<re2:
                re2=M-re1
                result=re1
print(result)
