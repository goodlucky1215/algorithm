import sys


def long_function_name(
        var_one, var_two,
        var_three, var_four):
    print()
var_one=var_two=var_three=var_four=4
#1. 인덴트(indent, 들여쓰기) : 파이썬은 공백 4칸 들여쓰기가 원칙이다.
#ver1 : 첫 번째 줄 파라미터가 있다면 두 번째 줄도 파라미터 위치를 같게 맞추기
foo = long_function_name(var_one, var_two,
                       var_three, var_four)
#ver2 : 첫 번째 줄에 파라미터가 없다면 공백 4칸 인덴트를 한 번 더 추가해 행을 구분한다.
def long_function_name(
        var_one, var_two,
        var_three, var_four):
    print(var_one)

#2. 네이밍 컨벤션 : 파이썬은 스네이크 케이스
#파이썬은 파이썬 방식에 자부심이 있어 카멜 케이스는 지양하고 "스네이크 케이스"fmf tjsghgksek.
#면접관이 질문하게 되면 파이썬의 PEP8 및 철학에 따라 스네이크 코딩을 했다고 말해야한다.
#실제로 연구결과에 따르면 카멜케이스보다 스네이크 케이스 방식이 더 인지하기 쉬웠다고한다.
camelCase = 1
snake_case = 1

#3. 타입 힌트
# 버그를 예방 하기 위해서 타입을 명시하는 것을 추천한다.
# mypy를 사용하면 타입 힌트에 오류 확인 가능. 온라인 코딩 테스트에도 자동으로 확인 가능하니 사용하자
#전
a = "1"
b = 1
def fn(a):
    return False;

#후
a: str = "1"
b: int = 1
def fn(a : int) -> bool: #파라미터 타입(int)과 리턴 타입(bool) 지정
    return False;

#4. 리스트 컴프리헨션
# 기존 리스트를 기반으로 새로운 리스트를 만들어내는 구문
# 람다 표현식에 map이나 filter를 섞어서 사용하는 것에 비해 가독성이 훨씬 높다

#람다_list
result=list(map(lambda x: x+10, [1,2,3]))
print(result)

#리스트 컴프리헨션_list
result=[x+10 for x in [1,2,3]]
print(result)
result=[n*2 for n in range(1,10+1) if n%2 ==1]
print(result)

original = {"rabbit":"orange", "hamster":"blue", "puppy":"brown"}
#일반 딕셔너리
a={}
for key, value in original.items():
    a[key]=value
print(a)

#리스트 컴프리핸션_딕셔너리
a={key: value for key, value in original.items()}
print(a)

#5. 제너레이터
# 루프의 반복 동작을 제어할 수 있는 루틴 형태이다. yield구문을 사용하면 제너레이터를 리턴할 수 있다.
# 예를 들어 숫자 1억개를 계산하는 프로그램이 있다면
# 제너레이터가 없다면 메모리 어딘가에 숫자 1억개를 보관해야한다.
# 제너레이터가 있다면 단순히 제너레이터만 생성해두고 필요할 때 언제든 숫자를 만들어낼 수 있다.
def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n
# 100개의 값을 생성하고 싶다면 100번동안 next()를 수행하면 된다.
g = get_natural_number()
for _ in range(0,100):
    print(next(g))
# 제너레이터는 여러 타입의 값을 하나의 함수에서 생성하는 것도 가능하다.
def generator():
    yield 1
    yield 'string'
    yield True
g = generator()
print(next(g))
print(next(g))
print(next(g))

#6. range() : 제너레이터 방식을 쓰는 대표적인 함수
# 파이썬 버전 3.x 이후로 range() 함수가 제너레이터 역할을 하는 range 클래스를 리턴하는 형태가 됨.
a = list(range(5))
print(a)
for i in range(5):
    print(i, end=' ')
print()
# 숫자 100만개를 생성하는 방법 2가지
a = [n for n in range(1000000)]
b = range(1000000)
print(len(a) == len(b)) # True : 둘 다 100만개로 나옴
print('a List : ',type(a),', b List : ', type(b)) # a List :  <class 'list'> , b List :  <class 'range'>
print('a size : ',sys.getsizeof(a),', b size : ', sys.getsizeof(b)) # a size :  8448728 , b size :  48
# => 똑같이 100만개를 생성하지만,
# => range 사이즈(메모리 점유율)가 훨씬 작을 것을 알 수 있다.
# why? range는 값을 보관하는게 아닌 생성 조건만을 보관하기 때문이다. 인덱스 접근도 가능하다. 그때 바로 생성해서 구현된다.

#7. enumerate : 여러 가지 자료형(list, set, tuple 등)을 인덱스를 포함한 enumerate 객체로 리턴한다.
a = [1,45,'a','c']
enumerate(a)
lists = list(enumerate(a))
print(lists) # [(0, 1), (1, 45), (2, 'a'), (3, 'c')]
#리스트를 인덱스와 함께 값 출력하는 방법
a = ['a1','a2','a3']
#방법1
for i in range(len(a)):
    print(i, a[i], "/", end=' ')
print()
#방법2
i = 0
for v in a:
    print(i, v, "/", end=' ')
    i+=1
print()
#방법3
for i, v in enumerate(a):
    print(i, v, "/", end=' ')
print()

#8. 나눗셈 연산자 : / 는 나눗셈, / 는 몫, % 는 나머지
print("나눗셈 : ",5/3, "type : ",type(5/3))
print("몫 : ",5//3, "type : ",type(5//3))
print("나머지 : ",5%3, "type : ",type(5%3))

#9. print
# 콤마(,)로 구분하면된다. 구분자는 한 칸 공백이 디폴트 설정되어있다.
print('a','b')
# sep파라미터로 구분자를 지정해줄 수 있다.
print('a','b',sep=',')
# print() 함수는 항상 줄바꿈을 한다.
print('a')
print('b')
# end파라미터를 공백으로 처리하여 줄바꿈을 하지 않도록 할 수 있다.
print('a',end='')
print('b')
# 리스트를 출력할 때는 join으로 묶어서 출력한다.
list_print = ['A','B']
print(list_print)
print(' '.join(list_print))
print(','.join(list_print))
# Quiz. 다음과 같이 idx에 1을 더해서 fruit와 함께 출력하는 방법은?
idx = 1
fruit = 'apple'
# 방법1 : 인덱스를 사용
print('{0}: {1}'.format(idx+1,fruit))
# 방법2 : 인덱스를 생략해서도 가능
print('{}: {}'.format(idx+1,fruit))
# 방법3 : f-string(formated string literal) => 인라인으로 삽입하는 방법
# 간렬하고 직관적이면 속도도 빠르다. 그러나 파이썬 3.6+ 이하 버전에서는 동작을 안한다.
print(f'{idx+1}: {fruit}')

#10. pass
# 코드 전체 골격을 잡고 코딩하는 경우가 생긴다.
# 예를 들어 아래와같이 메소드 이름만 생성해둔다.
'''
class MyClass(object):
    def method_a(self):
    
    def method_b(self):
    
c = MyClass()
이런식으로하면 그런데 이 클래스 자체가 실행이 안된다.
왜냐하면 method_a, method_b 안에 아무런 처리를 안했기 때문이다.
그래서 이러한 오류를 방지하는게 바로 pass이다.
'''
#오류가 나지않고 골격을 만들 수 있다.
#온라인코딩테스트 시에도 유용하게 활용할 수 있다.
class MyClass(object):
    def method_a(self):
        pass
    def method_b(self):
        pass
c = MyClass()

#11. locals : 로컬 심볼 테이블 딕셔너리를 가져오는 메소드, 업데이트도 가능
#로컬에 선언된 모든 변수를 조회할 수 있는 강력한 명령어
#로컬 스코프에 제한해 정보를 조회할 수 있다. 클래스의 특정 메소드 내부에서나 함수 내부의 로컬 정보를 조회해 잘못 선언한 부분을 체킹할 수 있다.
#변수명을 일일이 찾아보지 않고 로컬 스코프에서 정의된 변수를 출력해서 편리하다.
#클래스 메소드 내부의 모든 로컬 변수를 출력해 주기 때문에 디버깅에 많은 도움이 된다.
import pprint
pprint.pprint(locals())

#12. 구글 파이썬 스타일 가이드

#A. 함수에 기본 값으로 가변 객체(mmutable Object)를 사용하지 않아야 한다.
#함수가 객체를 수정하면 기본값이 변경되기 때문이다. 기본값으로 [] or {}를 사용하는 것은 지양해야 한다.

#지양하는 방법
from typing import Mapping, Optional


def foo(a, b=[]):
    pass
def foo(a, b: Mapping = {}):
    pass

#선호하는 방법
#불변 객체를 사용 => None을 명시적으로 할당하는 방법도 좋은 방법이다.
def foo(a, b=None):
    if b is None:
        b = []


class Sequeuce:
    pass


def foo(a, b: Optional[Sequeuce] = None):
    if b is None:
        b = []

#B. True, False를 판별할 때는 암시적인 방법을 사용하는 방법이 간결하고 가독성이 높다.
# 즉 False 임을 if foo != []: 보단 if foo: 로 충분하다.

#a. 길이 처리
users = []
#선호
if not users:
    print("no users")
#비선호
if len(users) == 0:
    print("no users")

#b. 정수를 처리할 때는 값을 직접 비교하는 편이 낫다.
#선호
if foo == 0 :
    print(foo)
#비선호
if foo is not None and not foo :
    print(foo)
#c. 명시적으로 값을 비교하는 편이 좋다.
i = 12
#선호
if i % 10 == 0:
    print(i%10)
#비선호
if not i % 10:
    print(i%10)

#C. 한 줄에 최대 줄 길이는 80자 이하로 한다.
