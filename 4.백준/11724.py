import sys
sys.setrecursionlimit(1000000000)
#상하좌우로 구역 같은지 비교
x=[1,0,-1,0]
y=[0,1,0,-1]
def per1(z1,i,j):
    for k in range(4):
        #각각의 구역 비교를 위해 인덱스값 더해줌
        x1=x[k]+i
        y1=y[k]+j
        #구역과의 z1[i][j]==z1[x1][y1]같고 인덱스 안에 있다면 들어감
        if 0<=x1<=n-1 and 0<=y1<=n-1 and z1[i][j]==z1[x1][y1]:
            if not z1_f[x1][y1]:#만약 아직 false라면
                z1_f[x1][y1]=True#true로 바꿔주고
                per1(z1,x1,y1)#끝날때까지 루프를 돌려줌

def per2(z2,i,j):
    for k in range(4):
        x1=x[k]+i
        y1=y[k]+j
        if 0<=x1<=n-1 and 0<=y1<=n-1 and z2[i][j]==z2[x1][y1]:
            if not z2_f[x1][y1]:
                z2_f[x1][y1]=True
                per2(z2,x1,y1)

n=int(input())#약 구역
#약 담을 통
z1=[]
z2=[]
#결과값
count1=0
count2=0
#ture,false로 같은 구역인지 아닌지 구별
z1_f=[]
z2_f=[]
for i in range(n):
    p=input()
    z1.append(p)#3가지색 구별하는 사람
    z2.append(p)#2가지색 구별하는 사람
    z2[i]=z2[i].replace('G','R')#2가지색 구별하는 사람은 한 색으로 교체
    z1_f.append([])
    z1_f[i]=[False]*n#아직 안지난 구역인 False로 만들어줌
    z2_f.append([])
    z2_f[i]=[False]*n#아직 안지난 구역인 False로 만들어줌    
for i in range(n):
    for j in range(n):
        if not z1_f[i][j]:#만약 안지난 구역 즉 false라면 루프를 돌려줌
            count1+=1#구역 갯수 증가
            z1_f[i][j]=True#지났으니 true로
            per1(z1,i,j)#같은 구역 표시
        if not z2_f[i][j]:
            count2+=1
            z2_f[i][j]=True
            per2(z2,i,j)
            
print(count1, count2)
        
    
