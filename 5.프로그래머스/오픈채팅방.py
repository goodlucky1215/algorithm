def solution(record):
    a={} #아이디를 담을 통
    for i in range(len(record)):
        record[i]=record[i].split(' ') #split로 나눠서 list 만들어줌
        if record[i][0] !='Leave': #Leave만 아니면 결국에 마지막에 나오는 닉네임이 진짜 닉네임
            a[record[i][1]]=record[i][2]#그러므로 계속해서 마지막까지 닉네임을 바꿔줌
    answer = [] #결과값
    for i in record: #앞에서부터 enter와 leave값 넣어줌!
        if i[0]=='Enter':
            answer.append(a[i[1]]+'님이 들어왔습니다.')
        elif i[0]=='Leave':
            answer.append(a[i[1]]+'님이 나갔습니다.')
    return answer
