def palindrome(s):
    qu=[]
    st=[]
    for x in s:
        if x.isalpha():#주어진 문자가 알파벳 문자에 해당하는지 확인하는 기능
            qu.append(x.lower())
            st.append(x.lower())
    while qu:
        if qu.pop(0) != st.pop():
            return False

    return True

print(palindrome("Wowowwowow"))
print(palindrome("Madam, I'm Adam."))
print(palindrome("Madam, I am Adam."))

def palindrome(s):
    n=[]
    for x in s:
        if x.isalpha():
            n.append(x.lower())
    for i in range(len(n)//2):
        if n[i] != n[-i-1]:
            return False
    return True

print(palindrome("Wowowwowow"))
print(palindrome("Madam, I'm Adam."))
print(palindrome("Madam, I am Adam."))
