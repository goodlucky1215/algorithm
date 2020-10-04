k=0
while True:
    l,p,v=map(int,input().split())
    if l==0 and p==0 and v==0:
        break
    k+=1
    #더 작은 값을 구할 땐 min을 사용하
    print('Case %d: %d' %(k,v//p*l+min(v-v//p*p,l))) 
