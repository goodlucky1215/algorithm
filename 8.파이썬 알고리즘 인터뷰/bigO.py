'''
1. 빅오란?
입력값이 무한으로 향할 때, 함수의 상한을 설명하는 수학적 표기 방법이다.

2. 시간복잡도 : 빅오 표기법의 종류
 (1). O(1) : 입력값이 아무리 커도 실행 시간이 일정. ex) 해시테이블의 조회 및 삽입
 (2). O(log n) : 매우 큰 입력값에도 영향이 적은 편. ex) 이진 검색
 (3). O(n) : 입력한 값 만큼 수행 시간이 비례. (선형 시간 알고리즘) ex) 정렬되지 않는 리스트에서 최댓값 or 최솟값 찾을 때
 (4). O(n log n) : 대부분 효율 좋은 알고리즘이 이에 해당. ex) 병합 정렬
 (5). O(n^2) : 비효율적인 정렬 알고리즘이 이에 해당. ex) 버블 정렬
 (6). O(2^n) : ex) 피보나치수를 재귀로 계산하는 알고리즘.
 (7). O(n!) : 가장 느린 알고리즘 ex) 브루트 포스

3. 공간 복잡도
- 시간과 공간이 트레이드오프 관계 : 실행 시간이 빠른 알고리즘은 공간을 많이 사용하고, 공간을 적게 차지하는 알고리즘은 실행 시간이 느리다.

'''

# O(n) , O(n^2) , O(2^n) 의 시간복잡도 예시
print("[ O(n) , O(n^2) , O(2^n) 시간복잡도 비교 ]")
for n in range(1,15+1):
    print(n, n**2, 2**n);

'''

4. 파이썬의 대표적인 자료형
 (1) None
 (2) 숫자  
 - 정수형 : 정수(int), 불리언(bool)  
 - 실수(float)  
 (3) 시퀀스
 - 불변 : 문자열(str), 튜플(tuple), 바이트(bytes)
 - 가변 : 리스트(list)
 (4) 집합형 - 중복된 값을 갖지 않는 자료형
 - 집합(set)
 (5) 매핑 - 키와 자료형으로 구성된 복합 자료형
 - 딕셔너리(dict)

A. int
 long 타입(임의정밀도 정수형)이 따로 없이 파이썬 버전3부터는 long타입이 int로 같이 사용된다.
 즉, int가 고정정밀도 정수형(int)가 임의정밀도 정수형(int,long)로 바뀌었다.
 임의정밀도란? 무한제 자릿수를 제공하는 정수형 => 정수를 숫자의 배열로 간주해서 이런일이 가능하도록 만들어졌다.
 임의 정밀도는 계산 속도가 저하되지만 숫자를 단일형으로 처리해 언어를 간단한 구조로 만들어준다.
  ex) int, long 구분되어 있으면 계산 오류나는 경험을 한 번씩은 해보았을 것이다.
 즉, 기능과 안전을 위해 속도를 맞바꾼 셈이다.
 자바같은 경우 int, long 따로 있지만, BigInteger로 임의 정밀도 자료형을 별도 제공하기도 한다.
 원시타입을 지원하지 않고 객체로 사용된다.
B. bool
 엄밀히 따지면 논리 자료형
 파이썬에서 내부적으로 1(True)과 0(False)로 처리되는 int 서브 클래스다.
 int는 Object의 하위 클래스이기도 해서 다음과 같은 구조라고 생각하면 된다.
 Object > int > bool
 
'''
#논리 자료형 True와 정수1 비교 예
print("[ 논리 자료형와 정수 비교 ]")
print(True==1)
print(False==0)

'''

C. 시퀀스
왜 문자열(str), 튜플(tuple), 바이트(bytes)는 불변이라고 할까?

'''
#a 값을 변경 전과 변경 후 주소가 다른 것을 확인할 수 있다.
# => 즉, 'abc'라는 값은 여전히 메모리 어딘가에 남아있다는 의미가 된다.
print("[ 시퀀스_불변 ]")
a = 'abc'
print("a의 주소 :",id(a))
a = 'def'
print("a의 주소 :",id(a))


'''
D. 파이썬은 모든 것이 객체이다.
- 불변 객체 : bool, int, float, tuple, str
- 가변 객체 : list, set, dict
주소를 비교해보면 불변과 가변의 차이를 쉽게 이해할 수 있다.
'''
a = 10
b = a
print("불변 객체의 주소 :",id(10), id(a), id(b))
a = 11
print("불변 객체의 주소 :",id(a), id(b))
print("불변 객체의 값 :",a, b) #a값을 바꿔도 b는 그대로의 주소를 갖는다.

a = [10,1,2]
b = a
print("가변 객체의 주소 :",id(a), id(b))
a[1] = 20
print("가변 객체의 주소 :",id(a), id(b))
print("가변 객체의 값 :",a, b) #a값을 바꾸면 주소를 따라가서 b값도 변한다.

'''

E. 비교 연산자 : is 와 ==
None(null)은 is로만 가능하다.
is로 비교하면 별도의 객체가 복사되어 다른 값을 갖는다.

'''
if a is None:
    print("aa")

a = [1,3,3]
print("a == list(a) :", a == list(a))
print("a is list(a) :", a is list(a))
