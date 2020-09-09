def find(m,n,a):
    k=set() #겹치는 것은 빼주는 set()을 사용
    for i in range(n-1): #얘가 지금은 행 역할을 함!!
        for j in range(m-1):
            if a[i][j] !='0': #만약에 0이 아닐때만(0은 이미 쓴 블록이므로)
                #4블록이 모두 같은 숫자라면
                if a[i][j]==a[i][j+1] and a[i][j]==a[i+1][j] and a[i][j]==a[i+1][j+1]:
                    k.add((i,j)) #각각의 모든 행,열을 set에 담아줌!
                    k.add((i,j+1))
                    k.add((i+1,j))
                    k.add((i+1,j+1))
    k=sorted(k) #정렬해줌(왜냐면 위에가 먼저 바뀌어야, 밑에의 인덱스에는 변화가 없으므로 피해않고 del 사용 가능)
    for i,j in k:
        del a[i][j]#먼저 없애주고
        a[i].insert(0,'0')#다시 위에 0인덱스에 '0'을 넣음
    return len(k),a
                                
def solution(m, n, board):
    answer = 0 #결과값
    a=[] #세로열로 값을 담음(세로로 블럭이 떨어지므로)
    for i in range(n): 
        a.append([])#세로열 만큼의 리스트를 만들기 위해서
        for j in range(m):
            a[-1].append(board[j][i])#각각의 가로열로 되어있는 board를 세로로 바꿔서 담음
    while True: #계속 돌림
        count,a=find(m,n,a) #터진블록수,바뀐 판을 저장
        answer+=count#터진 블록 수 더하기
        if count==0:#더이상 터질 블록이 없으므로 break
            break   
    return answer
