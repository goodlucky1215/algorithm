def find(i,z):
    b=z[:]
    for j in i:
        k=1
        while k<len(b):
            if j==b[k]:
                b[k-1]=str(eval(b[k-1]+b[k]+b[k+1]))
                b.pop(k)
                b.pop(k)
                k=1
            else:
                k+=1
    return abs(int(b[0]))
    
def solution(expression):
    a=[['*','-','+'],['*','+','-'],#모든 경우의 수
      ['+','-','*'],['+','*','-'],
      ['-','*','+'],['-','+','*']]
    b=[]#expression을 리스트 형태로 쪼갬
    k=''#숫자 담을 통
    for i in expression:
       if i not in '*-+': #숫자라면 
            k+=i #k에 넣어줌
       else:#연산 모양이라면
            b.append(k)#숫자를 넣고
            b.append(i)#연산 넣어줌
            k=''#다시 숫자 받을 통을 비워줌
    b.append(k)#마지막 숫자는 못 넣으므로 꼭 따로!!
    answer = 0#결과값
    for i in a:
       max_num=find(i,b)#
       if max_num>answer:#가장 큰 값인지 확인
            answer=max_num#큰 값이면 answer에 담기
    return answer
