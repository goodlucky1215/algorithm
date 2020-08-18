import sys
N, M=map(int,input().split()) #책 갯수, 박스 무게
if N==0: #만약 책이 0개라면 
    print(0) #그냥 0 출력하고
    sys.exit() #시스템 종료
a=list(map(int,input().split())) #책들의 무게 리스트값 넣기
box=1 #필요한 박스 수(출력값)
n=M #책의 무게를 뺄 n값 생성
for i in reversed(a): #쌓아진 책부터 빼므로 reversed해줘서 책 무게 계산
    n-=i #n으로 책 무게 뺀다
    if n<0: #만약 n이 -면 그 책을 그 박스엔 담을 수 없음
        box+=1 #새로운 박스를 꺼내서
        n=M #새로운 박스 무게를 만들어줌
        n-=i #그리고 다시 못 담았던 책 무게를 빼줌
        
print(box)
