def palindrome(s):
    q=[]
    u=[]
    for i in s:
        if i.isalpha():
            q.append(i.lower())
            u.append(i.lower())
    while q:
        if q.pop(0)!=u.pop():
            return False

    return True

print(palindrome("wow"))
print(palindrome("woW"))

#큐와 스텍 이용하지 않고 회문 찾기
def palindrome(s):
    result=[]
    for i in s:
        if i.isalpha():
            result.append(i.lower())
    for i in range(len(result)//2):
        if result[i]!=result[-i-1]:
            return False

    return True

print(palindrome("wow"))
print(palindrome("woW"))
print(palindrome("madam, I am Adam."))

