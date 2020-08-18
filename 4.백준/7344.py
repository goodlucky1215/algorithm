n=int(input())

def l_w(s,l):
    p=[]
    j=[False]*s
    result=0
    for i in range(0,len(l),2):
        p.append(l[i:i+2])
    p.sort()
    for i in range(len(p)):
        if j[i] != True:
            start=p[i]
            j[i]=True
            for f in range(i+1,len(p)):
                if start[0]<=p[f][0] and start[1]<=p[f][1] and not j[f]:
                        j[f]=True
                        start=p[f]
            result+=1
    return print(result)
for i in range(n):
    s=int(input())
    l=list(map(int,input().split()))
    l_w(s,l)
