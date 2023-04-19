#1-1 : 루프
sum1 = 0
for i in range(1,10+1):
    sum1 +=i
print("sum : ", sum1);

#1-2 : 루프
sum1 = sum(i for i in range(1,10+1))
print("sum : ", sum1);

#1-3 : 루프
sum1 = sum(range(1,10+1))
print("sum : ", sum1)

#2-1 : 제네릭 프로그래밍
def are_equal(a,b):
    return a+b;

print("합 : ",are_equal(10,5))

#2-2 : 파이썬은 원래 동적 타이핑 언어라서 제네릭이 없다.
#    => 사용하기에는 편리하지만 타입이 명시되어있지 않으면 코드가 복잡해질수록 헷갈린다.(버그를 야기할 수도 있다.)
#       따라서 다음과 같이 타입을 명시에 가독성을 높일 수 있다.
from typing import TypeVar
T = TypeVar('T')
U = TypeVar('U')
def are_equal(a: T, b: U) -> bool :
    return a==b;

print("합 : ",are_equal(10,10.0));

#3 : 베열 반복
foo = ["a","b","c"]
for i in foo:
    print(i)

#4-1 : 구조체
# 파이썬은 구조체가 없고, 클래스 또한 데이터 타입을 지정할 수 없다.
# 구조체 같은 형태를 정의하려면 namedtuple을 사용
from collections import namedtuple
MyStruct = namedtuple("MyStruct", "f1 f2 f3")
m = MyStruct("foo","bar","bas")
print("nametuple 선언 : ",MyStruct)
print("값을 할당 : ",m)


#4-2 : 구조체 @dataclass
# 파이썬 3.7부터 dataclass를 지원 => 구조체 형태로 정의할 수 있게 되었다.
# @를 자바에선 어노테이션, 파이썬에는 데코레이션이라고 부른다.
# 3.6버전 이하인 경우 하위 호환성을 위해 백포트 버전도 제공
from dataclasses import dataclass

@dataclass
class Product:
    weight: int = None
    price: float = None
apple = Product()
apple.weight = 269
apple.price = 29000
print("사과 무게 : ",apple.weight,"g")
print("사과 가격 : ",apple.price,"원")

#5 : 클래스
# @dataclass 선언하지 않아도 클래스 구현은 가능. 그러나 선언하면 여러가지 내부 기능도 사용힐 수 있다.
@dataclass
class Rectangle:
    width: int
    height : int
    def area(self):
        return self.width * self.height
rect = Rectangle(3,4)
print("사각형 넓이 : ",rect.area(),"cm")