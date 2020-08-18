#팩토리얼 구하기
def fact(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s

print(fact(1))
print(fact(5))
print(fact(10))

#팩토리얼 구하기: 재귀 호출
def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)
    
print(fact(1))
print(fact(5))
print(fact(10))

#1~n 더하기: 재귀 호출
def sum_n(n):
    if n<=1:
        return 1
    return n+sum_n(n-1)

print(sum_n(1))
print(sum_n(10))
print(sum_n(100))

#최댓값 찾기: 재귀 호출
def max_n(n):
    if len(n)==1:
        return n[0]
    if n[0]>n[1]:
        n.pop(1)
    else:
        n.pop(0)
    return max_n(n)

v=[17,92,18,33,58,7,33,42]
print(max_n(v))

print()

def max_m(a,n):
    if n==1:
        return a[0]
    m=max_m(a,n-1)
    if m>a[n-1]:
        return m
    else:
        return a[n-1]
v=[17,92,18,33,58,7,33,108,42]
print(max_m(v,len(v)))
