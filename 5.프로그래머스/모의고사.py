#1번 풀이
def solution(answers):
    a=[0,0,0] #각각 사람마다 맞추는 수
    answer = []#결과
    #3명의 사람 케이스
    per1=[1,2,3,4,5]
    per2=[2,1,2,3,2,4,2,5]
    per3=[3,3,1,1,2,2,4,4,5,5]
    k=0#각 per에 해당하는 인덱스
    for i in answers:
       if per1[k]==i:
            a[0]+=1
       if k>3:#인덱스보다 크면 0으로
            k=0
       else:
            k+=1
    k=0
    for i in answers:
       if per2[k]==i:
            a[1]+=1
       if k>6:
            k=0
       else:
            k+=1
    k=0
    for i in answers:
       if per3[k]==i:
            a[2]+=1
       if k>8:
            k=0
       else:
            k+=1
    for i in range(3):
        if max(a)==a[i]: #제일 많이 맞춘 수와 같다면
            answer.append(i+1); #그 사람의 번호를 넣어

    return answer
#2번 풀이
def find(answers,i):
    count=0
    k=0
    for j in answers:
        if j==i[k]:
            count+=1
            k+=1
        else:
            k+=1
        if k>len(i)-1:
            k=0
    return count
def solution(answers):
    a=[[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    answer = []
    for i in a:
        answer.append(find(answers,i))
    p=[]
    for i in range(3):
        if answer[i]==max(answer):
            p.append(i+1)
    return p
