N,M,K=map(int,input().split())
s=[0]*N
for i in range(M):
    Gan=list(map(float,input().split()))
    
    for i in range(0,N*2,2):
        if s[int(Gan[i]-1)]<Gan[i+1]:
            s[int(Gan[i]-1)]=Gan[i+1]
s.sort(reverse=True)
print('%.1f' % sum(s[0:K]))
