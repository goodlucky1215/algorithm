def solution(participant, completion):
    a={} #선수를 담음
    answer = ''#못들어간 선수 1명
    for i in participant:
            if i not in a: #선수이름에 따른 사람 수1명씩 담음
                    a[i]=1
            else: #동명이인인 선수가 있다면 +1
                    a[i]+=1
    for i in completion: #통과한 선수
            if i in a: #통과한 선수 1명씩 뺌
                    a[i]-=1
            if a[i]==0:#만약 값이 0이라면 그 선수이름도 뺌
                    del a[i]#동명이인을 걸러내기 위하여 하는 거임
    for i in a:#값을 꺼내면 value값이 꺼내짐
            answer+=i#값 넣고 결과
    return answer
