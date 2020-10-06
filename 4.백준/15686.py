from itertools import combinations
n,m=map(int,input().split())
road=[]
home=[]
che=[]
for i in range(n):
    road.append(n)
    road[i]=list(map(int,input().split()))
    for j in range(n):
        if 1==road[i][j]:
            home.append([i,j])
        elif 2==road[i][j]:
            che.append([i,j])
resu=10**9
for i in list(combinations(che,m)):
        re=0
        for k in home:
            mi=10**9
            for j in i:
                p=abs(k[0]-j[0])+abs(k[1]-j[1])
                mi=min(p,mi)
            re+=mi
        resu=min(re,resu)
print(resu)
    
