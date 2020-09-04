import sys
n,m=map(int,input().split()) #n은 nxn행렬, m은 구할 값 수
a=[]#nxn차 행렬 받을 통
for i in range(n): #nxn행렬 입력
        a.append(list(map(int,sys.stdin.readline().split())))
        
for i in range(n):
    for j in range(1,n):
        a[i][j]=a[i][j-1]+a[i][j] #행끼리 왼쪽에서 오른쪽으로 몰아서 더해줌.
for i in range(m):
    q1,q2,q3,q4=list(map(int,sys.stdin.readline().split()))#구할 m갯수 입력
    re=0#출력값
    for j in range(q1-1,q3):#값이 1부터 시작하는데 인덱스 0부터 시작하므로 q1-1해줘야하고 range는 q3-1까지 구하므로 건드리지 않아도 됨. 
        if q2 !=1: #만약 q2가 1이 아니라면 위에서 행끼리 왼쪽에서 오른쪽으로 몰아서 더해줬으므로
            re+=a[j][q4-1]-a[j][q2-2]#q2-2해주면 구하려는 행에서 행까지의 값이 남으므로 re에 더해주면 됨.
        else:
            re+=a[j][q4-1]#만약 q2가 1이라면 시작점부터의 행렬이므로 q4-1까지의 행렬을 더해주면 됨(행렬은 0부터 시작하고 값은 1부터 시작하니 인덱스에 맞춰주렴 -1)
    print(re)#결과 출

