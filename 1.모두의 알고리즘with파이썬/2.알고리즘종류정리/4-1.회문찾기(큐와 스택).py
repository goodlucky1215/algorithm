#회문: 순서대로 읽어도 거꾸로 읽어도 그 내용이 같은 낱말이나 문장
#      회문을 확인하는 두 가지 기본적인 방법

#1. 큐: 줄서기, 가장 먼저 들어간 자료를 가장 먼저 꺼냄
#        인큐: 자료를 한 개 집어넣는 동작 / 디큐: 자료를 한 개 꺼내는 동작

#2.스택: 접시쌓기, 가장 마지막에 들어간 자료를 가장 먼저 꺼냄(거꾸로)
#        푸시: 자룔 하나 집어넣는 동작    / 팝: 자료를 하나 꺼내는 동작

#회문 찾기 알고리즘-큐&스택
def palindrome(s):
    qu=[]
    st=[]
    for x in s:
        if x.isalpha(): #isalpha 문자인지 확인하는 기능
            qu.append(x.lower()) #lower 문자를 소문자로 바꿈
            st.append(x.lower())
    while qu:
        if qu.pop(0) != st.pop():#pop()는 뒤에 문자부터 꺼내서 소거
            return False

    return True

print(palindrome("woW"))
print(palindrome("Madam, I'm Adam."))
print(palindrome("Madam, I am Adam."))

#다른 방법으로 회문 찾기 알고리즘  
def palindrome(s):
    i=0
    j=len(s)-1
    while i<j:
        if s[i].isalpha()==False:
            i +=1
        elif s[j].isalpha()==False:
            j -= 1
        elif s[i].lower() != s[j].lower():
            return False
        else:
            i +=1
            j -=1

    return True

print(palindrome("woW"))
print(palindrome("Madam, I'm Adam."))
print(palindrome("Madam, I am Adam."))
