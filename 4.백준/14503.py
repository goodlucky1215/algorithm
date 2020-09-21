def find(r,c,d,pla):
    #벽이거나 이미 청소한 구역일 경우
    #각각에 맞는 방향을 중심으로 / 넘지 않는 인덱스인지 확인하고 / 후진할 수 있는 지확인해서 가능하면
    #위치 옮기 안 된다면 루프 종료
    if (robot[r+1][c]==1 or (r+1,c) in pla) and (robot[r-1][c]==1 or (r-1,c) in pla) and (robot[r][c+1]==1 or (r,c+1) in pla) and (robot[r][c-1]==1 or (r,c-1) in pla):
        if d==0 and 0<=r+1<n and robot[r+1][c]!=1:
                pla.add((r+1,c))
                find(r+1,c,0,pla)
        elif d==2 and 0<=r-1<n and robot[r-1][c]!=1:
                pla.add((r-1,c))
                find(r-1,c,2,pla)
        elif d==1 and 0<=c-1<m and robot[r][c-1]!=1:
                pla.add((r,c-1))
                find(r,c-1,1,pla)
        elif d==3 and 0<=c+1<m and robot[r][c+1]!=1:
                pla.add((r,c+1))
                find(r,c+1,3,pla)
        else:
            return
    #청소하지 않은 구역이 있을 경우엔
    #방향 확인하고 / 넘지 않는 인덱스 인지 확인하고 / 아직 청소안한 구역이고 / 벽이아닌 먼지라면
    #그에 맞게 로봇을 움직이고 방향도 각각 바꿔줌
    #그러나 그게 아니라면 방향만 바꿔
    else:
        if d==0:
            if 0<=c-1<m and (r,c-1) not in pla and robot[r][c-1]==0:
                pla.add((r,c-1))
                find(r,c-1,3,pla)
            else:
                find(r,c,3,pla)
        elif d==2:
            if 0<=c+1<m and (r,c+1) not in pla and robot[r][c+1]==0:
                pla.add((r,c+1))
                find(r,c+1,1,pla)
            else:
                find(r,c,1,pla)
        elif d==1:
            if 0<=r-1<n and (r-1,c) not in pla and robot[r-1][c]==0:
                pla.add((r-1,c))
                find(r-1,c,0,pla)
            else:
                find(r,c,0,pla)
        elif d==3:
            if 0<=r+1<n and (r+1,c) not in pla and robot[r+1][c]==0:
                pla.add((r+1,c))
                find(r+1,c,2,pla)
            else:
                find(r,c,2,pla)
n,m=map(int,input().split()) #공간 갯수
r,c,d=map(int,input().split())#시작 점 r,c와 방향 d
robot=[]
for i in range(n):#벽인 1과 먼지 0표시
    robot.append(list(map(int,input().split())))
pla=set()#청소한 구역 set
pla.add((r,c))#로봇이 서있는 첫번째 장소 청소
find(r,c,d,pla)#루프돌림
print(len(pla))
