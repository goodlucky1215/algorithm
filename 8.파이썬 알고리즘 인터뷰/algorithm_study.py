'''
속도

1. list  : pop(0)    => 속도는 O(n)
   deque : popleft() => 속도는 O(1) #앞 뒤 모두 속도가 O(1)로 훨씬 빠르다.



'''
import functools
import sys

'''
[[[[[[[[[[[[[[[[ char ]]]]]]]]]]]]]]]]]]]

1. isalnum() : 영문자와 숫자를 찾아준다.


'''

'''
[[[[[[[[[[[[[[[[ string ]]]]]]]]]]]]]]]]]]]

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

'''
[[[[[[[[[[[[[[[[ list ]]]]]]]]]]]]]]]]]]]

1. sort VS sorted
sort 함수는 리스트명.sort( ) 형식으로 "리스트형의 메소드"이며 리스트 원본값을 직접 수정합니다. => 메모리를 더 쓰지 않음, return값 없음
sorted 함수는 sorted( 리스트명 ) 형식으로 "내장 함수"이며 리스트 원본 값은 그대로이고 정렬 값을 반환한다. => 메모리를 추가로 사용, return값 List

2. sort - lambda
sorted(e, key = lambda x : (첫번째 정렬 기준, 첫번째 값이 같을 경우 두번째 정렬 기준));

3. sorted - 정렬 옵션 key =
sorted(list, key = len) => len으로 하면 길이 순으로 정렬된다.
sorted(list, key = function) => 설정한 function으로도 정렬이 된다.
'''
e = [(1,3),(0,3),(1,4),(1,5),(0,1),(2,4)]
f = sorted(e, key = lambda x : (x[0],x[1])) # 첫번째 인자, 두번째 인자 모두 오름차순
print(f)
f = sorted(e, key = lambda x : (x[0],-x[1])) # 두번째 인자는 내림차순으로 변경
print(f)

c= ['aaaaaaaaaaaaaa','bbbb','cc','ddddddd']
print(sorted(c,key = len)) #길이가 가장 짧은게 앞으로 가는것을 확인할 수 있다.

c = ['abc','bcd','bza']
def func(str) :
    return str[0],str[-1]
print(sorted(c,key = func)) # 맨 첫글자로 정렬하고, 같으면 맨 마지막 글자로 비교 정렬하게 된다.
print(sorted(c,key = lambda s:(s[0],s[-1]))) # lambda형식으로도 가능하다.


'''
3. collections.Counter(list) : list에서 반복되는 문자와 갯수 추출 (문자,반복회수)
- collections.Counter(list).most_common(n) : n개 만큼의 제일 반복 많이 된 것부터 정렬
'''
import collections
paragraph_list = ['a','b','c','a','b','a','e']
paragraph_counter = collections.Counter(paragraph_list)
print(paragraph_counter)
paragraph_most = paragraph_counter.most_common(len(paragraph_counter))
print(paragraph_most)


'''
최댓값과 최솟값 초기값 지정 방법
'''
max_num = sys.maxsize
min_num = -sys.maxsize
#float를 이용해서 지정
max_num = float('-inf')
min_num = float('inf')

'''
링크드 리스트
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#생성
head = ListNode(0)
#추가 : 선언한 head를 이동하지 않고, 주소를 참소해서 다음 노드를 추가한다.
add_node = head
add_node.next = ListNode(1)
#출력
node = head
while node:
    print(node.val)
    node = node.next

'''
숫자형 리스트 단일 값으로 변경

1. map(function, iterable) : map(적용시킬 함수, 적용할 값들)

2. functools : 함수를 다루는 함수
   reduce(함수, 시퀀스) : 시퀀스(문자열, 리스트, 튜플)의 원소들을 누적적으로 함수에 적용
   
- 3번째 변수?
    a = [1,2,3,4,5]
    functools.reduce(lambda x,y:x*y,a,10) #여기서 마지막에 세번째변수 10
    초기값을 10으로 설정한 것으로, 간단히 설명하자면 다음과 같습니다.
    => ((((10 * 1) * 2) * 3) * 4) * 5)
    functools.reduce(lambda x,y:x*y,a)
    => (((1 * 2) * 3) * 4) * 5) 초기값이 없으면 2개 값부터 가지고 온다.
'''
a = [1,2,3,4,5]
int(''.join(map(str,a)))

functools.reduce(lambda x,y:x*10+y,a)

# 둘 다 결과는