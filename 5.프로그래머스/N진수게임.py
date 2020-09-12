def find(i,n):
    e='0123456789ABCDEF'#16진수까지 나올 수를 보여줌
    a,b=divmod(i,n)#i숫자를 n진수로 나눠줌 
    if a==0:#몫이 0이라면 계산 끝
        return e[b]#나머지의 진수 값만 뽑아냄
    else:
        return find(a,n)+e[b]#몫이 0될 때까지 계산해서 이어붙여줌
def solution(n, t, m, p):
    word=''#n진수 후에 나올 값들 넣어줌
    i=0#숫자 번호
    while len(word)<m*t:#m명의 사람들끼리 하고, 내가 t횟수까지 말해야하므로 적어도 갯수가  m*t까지는 알아야됨
        word+=find(i,n)#i의 n진수 찾아서 값 넣기
        i+=1#i숫자 올리기
    answer = ''#결과값
    for j in range(0,m*t,m):#m*t갯수 중에서 m씩 건너뛰어서 나의 p번째를 말하면 됨
        answer+=word[j+p-1]#j가 시작번호 p는 내 순서(-1은 인덱스번호는 0부터 시작하기 때문)
    
    return answer
print(solution(2,4,2,1))
