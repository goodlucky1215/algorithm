#팩토리얼-연속한 숫자의 곱 구하기
def fact(n):
    f = 1
    for i in range(1,n+1):
        f=f*i
    return f

print(fact(1))
print(fact(5))
print(fact(10))

#팩토리얼-'재귀 호출'로 구하는 알고리즘
def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)

print(fact(1))
print(fact(5))
print(fact(10))

#1~n까지 합 재귀 호출로 만들기
def sum_n(n):
    if n==1:
        return 1
    return n+sum_n(n-1)

print(sum_n(3))
print(sum_n(100))

#숫자 n개 중에서 최댓값 찾기 - 재귀 호출 만들기 ***이게 어려움***
def max_m(m,n):
    if n==1:
        return m[0]
    max_m_1 = max_m(m,n-1) #한개가 될 때까지 재귀 호출 시켜서 하나가 되면 값 비교 후,
    if max_m_1 > m[n-1]:   #그 값의 크기를 보고 다시 다음 값과 비교하고를 무한 반복
        return max_m_1
    else:
        return m[n-1]

v=[17,92,13,33,53,5,33,42]
print(max_m(v,len(v)))
