def solution(array, commands):
    answer = []#정답
    for i in commands:#각각의 자를 번호와 구하려는 i[2]의 숫자
        temp = array[i[0]-1:i[1]]
        temp.sort()#정렬 후에
        answer.append(temp[i[2]-1])#구하려는 i[2] 숫자 구함.
    return answer
