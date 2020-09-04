def solution(board, moves):
    doll=[] #인형 뽑을 통
    for i in moves: #인형 뽑을 열 번호
        for j in range(len(board)): #인형 뽑을 행에 인형 있는지 확인
            if board[j][i-1] != 0: #0이 아니고 숫자면 인형이 존재
                doll.append(board[j][i-1])#그렇다면 인형통에 넣어주고
                board[j][i-1]=0#그에 해당하는 행과 열에서는 인형이 없으니 값 0으로
                break #빼면 멈추고 moves로 다음 열 확인(없다면 끝 행까지 for j가 돌아가겠지?!!)
    answer = 0 #결과값(인형 수)
    i=0 #doll에서 같은 인형이 차례로 있는지 확인하기 위한 인덱스 번호
    while i<len(doll)-1:#i가 doll인덱스보다 작다면 이 루프는 계속 돌아감
        if doll[i]==doll[i+1]:#i인덱스와 i+1인덱스의 인형이 같다면(숫자가 같다면) 인형이 사라짐.
            answer+=2 #*****결과값에 사라지는 인형 갯수 추가
            doll.pop(i+1)#***주의*** i+1부터 무조건 처리!!!!(i부터 pop)하면 인형이 앞으로 당겨지기 때문
            doll.pop(i)#아니면 pop(i)를 두번 처리해도 됨~
            i=0#인형이없어지면 다시 앞부터 비교해야됨(두 인형땜에 만나지 못한 같은 인형이 있을 수 있으므로)
        else:
            i+=1 #i인덱스와 i+1인덱스가 같지 않다면 인덱스 번호가 같을 때까지 계속 비교
        
    return answer
