def solution(msg):
    eng={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,
        'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,
        'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}#숫자들 dic에 넣어줌
    answer = []#결과값
    f=27 #다음 dic이 들어올 때 받을 숫자
    w,c='','' #w는 시작 번호, c는 다음 번호
    for i in range(len(msg)-1):    
        w+=msg[i]#처음 번호 받고
        c+=msg[i+1]#다음 번호 받음
        answer.append(ang[w])#처음 번호의 번호 넣어줌
        if w+c in ang:#하지만 w+c 번호가 이미 있는 단어라면
            answer.pop()#다시 번호를 뺌
        else:
            ang[w+c]=f#w+c가 없는 번호라면 새로 dic에 넣어줌
            f+=1#dic 숫자 +1 해줌
            w=''#w는 새로 받아야하므로 비워줌
        c=''#다음에 새로운 단어를 받아야하므로 무조건 비워줌
    w+=msg[-1]#마지막 번호는 따로 넣어줌
    answer.append(ang[w])#그리고 넣어줌
     
    return answer
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
