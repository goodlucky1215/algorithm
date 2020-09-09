def find(i,s):
    result,a="",s[0:i] #결과값,같은 단어인지 비교할 통
    k=1#연속된 같은 단어 갯수
    for j in range(i,len(s),i):#모든 단어 비교
        if s[j:j+i]==a:#같은 단어라면
            k+=1#단어 갯수 +1
        else:#같은 단어가 아니라면
            if k!=1:#만약 1개 아닐시엔
                result+=str(k)#같은 단어 갯수 수를 넣어주고
            result+=a#단어를 더해줌
            k=1#다음 단어는 다시 1개부터 카운팅
            a=s[j:j+i]#단어도 바꿔서 비교
    #*******마지막 단어는 못들어가므로 한번 굴려서 넣어주기~*****            
    if k!=1:
        result+=str(k)+a
    else:
        result+=a
    
    return len(result)
   
def solution(s):
    answer = len(s)
    for i in range(1,len(s)//2+1):#모든 경우의 수 다 계산(문자열을 똑같이 쪼개므로 1/2까지만 하면됨)
        z=find(i,s)
        if z<answer:#만약 더 짧다면 바꿔줌
            answer=z
    return answer
