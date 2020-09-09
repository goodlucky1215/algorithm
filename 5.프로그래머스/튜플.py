def solution(s):
    s=s[1:-1] #첫번째와 마지막 { }없애줌!
    a=[]#s의 숫자들을 리스트 형태로 담음
    k=''#str을 int로 바꿔줄 통
    for i in s:
        if i=='{': #새로운 리스트 생성의미
            a.append([])
        elif i!='}':# } 이 아닌 경우
            if i==',':#','일때는 숫자가 완성된 후므로
                a[-1].append(int(k))#k를 int형으로 바꿔서 리스트에 넣어줌
                k=''#새로운 숫자를 받기 위해서 통 비워줌
            else:
                k+=i#','가 아니면 계속 이어진 숫자가 안 끝났으므로 숫자를 붙여줌
    a[-1].append(int(k))#마지막에 나온 숫자는 넣지 못하므로 for 후에 넣어주기!!!
    a=sorted(a,key=lambda a:len(a))#각 리스트 길이에 따라서 정렬
    answer = [] #결과값
    for i in a: #가장 짧은 길이의 리스트부터 나오므로
        for j in i:
            if j not in answer: #없는 값을 뽑기만 하면됨
                answer.append(j)
                break #뽑고나면 break로 for j문은 나와도 됨(각 리스트에는 하나의 새로운 숫자만 추가되므로)
    return answer
