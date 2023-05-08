'''
속도

1. list  : pop(0)    => 속도는 O(n)
   deque : popleft() => 속도는 O(1)



'''


'''
char

1. isalnum() : 영문자와 숫자를 찾아준다.


'''

'''
string

1. 슬라이싱 [::-1] : 글자를 뒤집을 수 있다. 내부적으로 C로 구현되어있어서 빠르다.
'''

'''

1. 정규표현식 regex
(1) sub(패턴, 교체할 문자열, 문자열, 최대 교체 수, 플래그)
    re.sub('[^a-z0-9','',s) # s문자열 안에 영어와 숫자 아닌건 전부 ''(빈칸)으로 만들어버린다.

'''
import re
print(re.sub('a', 'z', 'ab')) # zb
print(re.sub('a', 'zxc', 'ab')) # zxcb
print(re.sub('a', 'z', 'aaaab')) # zzzzb
print(re.sub('a', 'z', 'aaaab', 1)) # zaaab => 갯수 지정
