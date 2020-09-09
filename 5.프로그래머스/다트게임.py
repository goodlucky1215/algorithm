def solution(dartResult):
    b=[0,0,0,0]
    k=0
    for i in range(len(dartResult)):
        if dartResult[i]=='S':
            b[k]**=1
        elif dartResult[i]=='D':
            b[k]**=2
        elif dartResult[i]=='T':
            b[k]**=3
        elif dartResult[i]=='#':
            b[k]*=(-1)
        elif dartResult[i]=='*':
            b[k-1]*=2
            b[k]*=2
        else:
            if dartResult[i+1] !='0':
                if i>0:
                    if dartResult[i-1] !='1':
                        k+=1
                b[k]+=int(dartResult[i])  
            else:
                k+=1
                b[k]+=10
    answer=sum(b)
    return answer

def solution(dartResult):
    dart=[0,0,0,0] #다트를 담을 통
    k=0#다트 인덱스
    for i in dartResult:
        #각 값에 따라서 계산
        if i=='S': 
            dart[k]**=1
        elif i=='D':
            dart[k]**=2
        elif i=='T':
            dart[k]**=3
        elif i=='*':
            dart[k-1]*=2
            dart[k]*=2
        elif i=='#':
            dart[k]*=(-1)
        else:
            #숫자가 들어오면
            if i=='0': #0일때
                if dart[k]==1: #만약에 앞글자가 1이라면 이 다트는 10점짜리임
                    dart[k]+=9#따라서 처음에 1더해줬으므로 9를 더 더해줌.
                else:
                    k+=1#만약에 앞 숫자가 1이아니라면 이 다트는 새로운 0점 짜리 다트므로 k+=1
            else:
                k+=1 #만약 0이아니면 새로운 다트판이므로 k+=1
                dart[k]+=int(i)#얻은 점수를 더해줌
        answer = sum(dart)#모든 다트 점수 
    return answer
