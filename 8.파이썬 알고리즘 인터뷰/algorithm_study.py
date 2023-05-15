'''
속도

1. list  : pop(0)    => 속도는 O(n)
   deque : popleft() => 속도는 O(1)



'''

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
'''
e = [(1,3),(0,3),(1,4),(1,5),(0,1),(2,4)]
f = sorted(e, key = lambda x : (x[0],x[1])) # 첫번째 인자, 두번째 인자 모두 오름차순
print(f)
f = sorted(e, key = lambda x : (x[0],-x[1])) # 두번째 인자는 내림차순으로 변경
print(f)
c= ['aaaaaaaaaaaaaa','bbbb','cc','ddddddd']
print(sorted(c,key = len)) #길이가 가장 짧은게 앞으로 가는것을 확인할 수 있다.
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