N,L=map(int,input().split()) #물웅덩이 갯수,널빤지 길이
info=[]#물 웅덩이의 리스트
start=0 #널빤지의 시작 위치
result=0#필요한 널빤지 최소 갯수
for i in range(N): #물 웅덩이 입력 받기
    info.append(list(map(int,input().split())))
info.sort() #물 웅덩이를 시작점을 기준으로 정렬

for i in range(N):
    #필요한 웅덩이 길이 계산하기 위한 load 생성
    if info[i][0]<=start: #만약 start가 시작점보다 크다면,
        load=info[i][1]-(start+1) #웅덩이의 끝지점-start부터 계산(+1하는 이유는 start까지에 널빤지가 채워져 있음)
    else:
        load=info[i][1]-info[i][0] #start보다 시작점이 더 크다면, 끝지점-시작점
    #load에서 널빤지의 갯수 계산
    if load%L>0:#load를 널빤지로 나눴을 때, 나머지가 있다면 
        nul=load//L+1 #웅덩이를 다 막기위해서 널빤지가 하나 더 필요
    else:
        nul=load//L #나머지가 없다면 웅덩이길이 나누기 널빤지
    result+=nul #필요한 널빤지 갯수를 결과값에 더해줌
    #이게 중요! start가 만약 다음 웅덩이를 감쌀만큼의 널빤지가 된다면, 다음 웅덩이는 시작점이 start로 바꿔줘야함!
    if info[i][0]<=start: #만약 start가 시작점보다 크다면,
        start=start+nul*L #start에다가 널빤지갯수와 웅덩이길이 곱해서 더해주면, 그 다음 start가 주어짐
    else:
        start=info[i][0]+nul*L-1 #start보다 시작점이 더 크다면, start는 시작점에서 널빤지갯수x웅덩이길이
    
print(result)
