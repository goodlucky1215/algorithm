import copy
n,m,v=map(int,input().split())#정점갯수, 간선 갯수, 탐색 시작번호
line={}#각 번호의 간선 수들 넣기
for i in range(1,n+1):
    line[i]=[]
for i in range(m):
    x,y=map(int,input().split())
    line[x].append(y)#각 번호의 간선 수 넣기
    line[y].append(x)
for i in range(1,n+1):
    line[i].sort()#정렬해서 정점 번호가 작은 것 부터
line1=copy.deepcopy(line)
re=[]#dfs결과값
p=[v]#시작 점
while p:
    i=p.pop(0)
    if i not in re:#아직 안들어온 값이라면
        re.append(i)#넣어주고
        p=line1[i]+p# 그값을 더 깊이 탐색해야하므로 앞에다가 더해서 넣어줌
print(*re)#dfs 결과
line1=copy.deepcopy(line)
p=line1[v]
re=[v]
while p:
    a=[]
    for i in p:#bfs는 순서대로 넣어줘야하므로 전부다 확인
        if i not in re:
            re.append(i)#안들어온 값이면 넣어주고
            a+=line1[i]#애는 뒤에다가 더해
    p=a
print(*re)


