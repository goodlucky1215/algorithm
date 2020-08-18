N=int(input()) #소의 수이자, 담을 수 있는 일 수
a=[] #소의 우유양, 소의 유통기한 담을 리스트
b=[False]*N #담은 날짜인지 아닌지 확인하기 위한 리스트
k=N-1 #소의 유통기한이 클 시,담을 수 있는 날짜(b)에 넣기 위한 k
result=0#총 최대 우유양(결과값)
for i in range(N): #소 우유랑, 유통기한 입력
    a.append(list(map(int,input().split())))
a.sort(reverse=True) #제일 많은 우유양을 가진 소부터 담아야하므로, sort와 reverse
for i in a: #차례대로 소의 우유[0]과 유통기한[1]을 뺀다
    #날짜는 뒤에서 부터 담는게 맞음!앞에는 기한이 짧은 우유들이 들어갈 수 있어야하므로!
    if i[1]>N: #만약 유통기한이 담는 날짜 기한보다 길 때,
        while k>=0: #k는 담을 수 있는 인덱스 값이므로 0보다 크거나 같아야함.
            if not b[k]: #b[k]에 아직 안담겨 있다면(False라면)
                b[k]=True #담아줌. 즉 True
                result+=i[0] #담았으므로 그 만큼의 우유 양을 더해줌
                break #담았으므로 break!
            else:
                k-=1 #만약 b[k]에 이미 담았다면(True) 인덱스k=-1을 해줘서 전 날짜확인.
    else:
        if not b[i[1]-1]: #유통기한이 담는 날짜 안에 존재한다면, 그 날짜에 우유를 안담았다면
            b[i[1]-1]=True #우유를 담아줌
            result+=i[0] #담았으므로 그 만큼의 우유 양을 더해줌
        else:
            c=-2 #해당 날짜에 담았다면 그 전 날짜의 담을 수 있는지 인덱스 확인
            while i[1]+c>=0: #인덱스는 0보다 크거나 같아야함
                if not b[i[1]+c]: #만약 아직 안담긴 날짜라면,
                    b[i[1]+c]=True #우유를 담아줌
                    result+=i[0] #담았으므로 그 만큼의 우유 양을 더해줌
                    break #담았으므로 정지
                else:
                    c-=1 #이미 담은 일 수라면 전 날짜에는 또 담을 수 있는지 다시 확인
print(result)
                
