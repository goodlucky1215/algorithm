def find(a,b):
    if len(a)<=len(b): #b의 번호길이가 더 길다면
       if b[:len(a)]==a:#a길이 만큼 잘라서 비교해서 같다면 false
                return False
    else:
        if a[:len(b)]==b: #a의 번호 길이가 더 길다면,b길이만큼만 비교해서 봄(그래서 for j가 처음부터 안돌고 i자리부터 돌 수 있음)
                return False

def solution(phone_book):
    answer=True#정답
    for i in range(len(phone_book)): #모든 번호 갯수
        for j in range(i+1,len(phone_book)):#i+1부터해서 차례로 비교
            if find(phone_book[i],phone_book[j])==False: #find를 통해서 비교
                answer = False#false가 나오면 for j문 종료
                break
        if answer==False:#false가 나오면 for i문 종료
            break
    return answer
