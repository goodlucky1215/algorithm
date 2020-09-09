import itertools
a=[False]*10000000
a[0]=True;
a[1]=True;
for t in range(2,len(a)): #소수들만 flase로 만들
    if not a[t]:
        for j in range(t*2,len(a),t):
            a[j]=True

def solution(numbers):
    b=set()
    answer = 0
    for i in range(len(numbers)):
       x=list(itertools.permutations(numbers,i+1))#모든 경우의 수 뽑기
       for j in x:
           s=''#숫자 담을 통
           for k in j:
               s+=str(k)#숫자를 문자로 변경해서 이어붙여서 만들기(2자리수,3자리수,n자리수 만들기 위해서)
           b.add(int(s))#마지막에 숫자형을 변환에서 넣어줌
    for i in b:
        if a[i]==False:#만약 false이면 소수 이므로 +1
            answer+=1
    return answer
print(solution('17'))
