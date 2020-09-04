def solution(numbers, hand):
    #키패드 딕셔너리 자료형으로
    phone={
        1:[0,0],2:[0,1],3:[0,2],
        4:[1,0],5:[1,1],6:[1,2],
        7:[2,0],8:[2,1],9:[2,2],
        '*':[3,0],0:[3,1],'#':[3,2]
    }
    answer = '' #결과값
    L='*' #시작 왼손
    R='#' #시작 오른손
    for i in numbers:
        if i==1 or i==4 or i==7 or i=='*': #왼손 키패드는 왼손으로
            answer+='L' 
            L=i #왼손 값 저장
        elif i==3 or i==6 or i==9 or i=='#':#오른손 키패드는 오른손으로
            answer+='R'
            R=i #오른손 값 저장
        else: #가운데 키패드일때
            a=abs(phone[L][0]-phone[i][0])+abs(phone[L][1]-phone[i][1])
            b=abs(phone[R][0]-phone[i][0])+abs(phone[R][1]-phone[i][1])
            if a<b: #왼손 값과 오른손 값 중 더 작은 움직인 손으로 키패드 이동
                answer+='L'
                L=i
            elif a>b:
                answer+='R'
                R=i
            else:#왼손, 오른손 움직이는 수가 같다면, 왼손잡이인지 오른손잡이인지 구별
                if hand=='left':
                    answer+='L'
                    L=i
                else:
                    answer+='R'
                    R=i
        
    return answer
