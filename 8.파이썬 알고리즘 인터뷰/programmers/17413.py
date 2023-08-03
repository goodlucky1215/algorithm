import sys
input = sys.stdin.readline
s = input().strip()
result = ''
word = ''
check = False # True이면 < 를 만난것
for i in s:
    if i=='<':
        if len(word) > 0:
            result += word[::-1]
            word = ''
        result+=i
        check=True
    elif i=='>':
        result+=i
        check=False
    elif check:
        result+=i
    elif i==' ':
        result+=word[::-1]
        result+=i
        word=''
    else:
        word+=i
if len(word)>0:
    result += word[::-1]
print(result)
