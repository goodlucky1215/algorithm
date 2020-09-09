import math
def solution(str1, str2):
    #영어 아닌 문자가 포함된 단어는 버리므로 걸러주기 위해서 만듬
    alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    str1=str1.lower() #둘이 비교를 위해서 둘다 소문자로 바꿈
    str2=str2.lower() #소문자열로 바꿈
    str11,str22={},{} #key는 단어, value는 key단어가 나온 횟수(중복으로 단어를 얻는다면 그 또한 집합안에 담아줘야 하므로) 
    for i in range(len(str1)-1):#단어를 2개씩 잘라서 담아주기
        word=True#이게 false이면 영어가 아닌 문자를 포함한 단어임
        for j in str1[i:i+2]:
            if j not in alpha: #만약 알파벳 아닌 문자라면
                word=False #word를 False로
        if word:#만약 문자 두글자가 다 영어라면
            if str1[i:i+2] not in str11:#아직 str1에 안 담겨진 단어라면 새로 담아줌
                str11[str1[i:i+2]]=1
            else:
                str11[str1[i:i+2]]+=1 #이미 담겨진 단어라면 그 중복 단어를 +1해줌
    for i in range(len(str2)-1):#위와 같이 구해줌
        word=True
        for j in str2[i:i+2]:
            if j not in alpha:
                word=False
        if word:
            if str2[i:i+2] not in str22:
                str22[str2[i:i+2]]=1
            else:
                str22[str2[i:i+2]]+=1
    gu,ha=0,0 #교집합, 합집합
    for i in str11: #str11의 key를 꺼냄
        if i in str22:#만약 str22의 key에있다면
            gu+=min(str11[i],str22[i])#최소 갯수는 교집합에
            ha+=max(str11[i],str22[i])#최대 갯수는 합집합에
        else:#str11만 가지고 있는 key라면
            ha+=str11[i]#합집합에만 값 넣어줌
    for i in str22:
        if i not in str11: #str22만 가지고 있는 key라면
            ha+=str22[i] #합집합에만 값 넣어줌
    if gu==0 and ha==0: #둘다 0이면 공집합 이므로 1로 취급해서 *65536
        return 65536
    elif gu==0 or ha==0: #둘 중 하나만 0이면 나누기할때, 런타임에러-->따라서 그냥 0으로 계산
        return 0
    else:#나머지는 계산해서 결과
        return math.trunc(gu/ha*65536)
