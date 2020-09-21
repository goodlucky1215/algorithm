n=int(input()) #아이템갯수
m=int(input()) #입력받을 아이템 값
a=[]
for i in range(n):#행렬 형태로 아이템 갯수 받음
    a.append([])
    a[i]=[0]*n
for i in range(m):
    x,y=map(int,input().split())#x>y
    a[x-1][y-1]=2#더 큰 애는 2로
    a[y-1][x-1]=1#작은 애는 1로
for k in range(n):
    for i in range(n):
        for j in range(n):
            if a[i][k]!=a[j][k]: #망약 두 행렬 값이 같지 않을 때
                if a[i][k]!=0 and a[j][k]!=0:#둘 다 0이 아니라면
                    if a[i][k]>a[j][k]:#더 큰 값을 가진 인덱스에게 2를 작은애한테는 1부여
                        a[i][j],a[j][i]=2,1
                    else:
                        a[i][j],a[j][i]=1,2
for i in a:
    print(i.count(0)-1)#그래서 0갯수들이 순위를 알 수 없는 애들임을 알 수 잇음(자기 자신인 0은 빼주므로 -1)
