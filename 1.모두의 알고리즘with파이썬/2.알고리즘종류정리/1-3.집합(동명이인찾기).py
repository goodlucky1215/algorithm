#set() - 집합 만들기
#discard(x)- 집합에 x가 있다면 삭제를 함.
# x in s - 어떤 자료 x가 집합s 에 들어있다면 true/ 아니면 false

#동명이인을 찾는 알고리즘-> **중첩된 반복문** 계산 복잡도는? O(n^2)
def find_same_name(a):
    n = len(a)
    result = set()
    for i in range(0,n-1):
        for j in range(i+1,n):
            if a[i]==a[j]:
                result.add(a[i])
    return result

name= ['tommy','jinny','harry','tommy','jin']
print(find_same_name(name))

#3-1 짝을 지울 수 있는 모든 경우
def find_partner(a):
    n = len(a)
    for i in range(0,n-1):
        for j in range(i+1,n):
            print(a[i],'-',a[j])
            
name1= ['tommy','jinny','harry']
name= ['tommy','jinny','harry','jin']
print(find_partner(name1))
print(find_partner(name))
