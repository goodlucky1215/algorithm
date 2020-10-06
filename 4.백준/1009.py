num=[[10],[1],[2,4,8,6],[3,9,7,1],[4,6],[5],[6],[7,9,3,1],[8,4,2,6],[9,1]]
for i in range(int(input())):
    k,m=map(int,input().split())
    k=int(str(k)[-1])
    k=num[k]
    m=m%len(k)-1
    print(k[m])
