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
