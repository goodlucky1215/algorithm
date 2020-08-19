n,m=map(int,input().split()) #행과 열
b=[] #행과 열을 받을 입력 값 리스트
c=[] #결과값
for i in range(n): 
    c.append([])
    b.append(list(map(int,input().split()))) #입력값
    c[i]=[0]*m #각 행마다 m만큼의 0값 만들기
c[0][0]=b[0][0] #시작점은 고정 시켜줌
for j in range(1,m): #첫 번째 줄(0행)은 어차피 비교할 값이 없으므로
    c[0][j]=b[0][j]+c[0][j-1] #각 각의 값을 더해줌. -->이때 b값 넣어주는거 주의
for j in range(1,n): #첫 번째 0열도 마찬가지로 비교할 값이 없으므로
    c[j][0]=b[j][0]+c[j-1][0] # 각 각의 값을 더해줌
for i in range(1,n): #이제 1행1열부터 비교하면됨. 대각선만 더하는 것은 어차피 값이 더 작으므로 의미가 없음
    for j in range(1,m): 
        if c[i-1][j]>=c[i][j-1]: #+1행과 +1열 한 값을 비교해서 더 큰 값을
            c[i][j]=b[i][j]+c[i-1][j]#i,j에 넣어 주면 됨.
        else:
            c[i][j]=b[i][j]+c[i][j-1]
print(c[n-1][m-1]) #그렇게하면 최댓값이 나
