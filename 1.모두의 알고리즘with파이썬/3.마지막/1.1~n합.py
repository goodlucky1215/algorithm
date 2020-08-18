# 1~n 합: 기본으로풀기
def sum_m(n):
    d=0
    for i in range(n+1):
       d+=i
    return d

print(sum_m(10))
print(sum_m(100))

# 1~n 합: 가우스공식으로 풀기
def sum_m(n):
    return n*(n+1)//2

print(sum_m(10))
print(sum_m(100))

# 제곱의 합 : 기본으로 풀기
def sum_m(n):
    d=0
    for i in range(n+1):
        d+=i**2
    return d

print(sum_m(10))
print(sum_m(100))

# 제곱의 합 : 공식으로 풀기
def sum_m(n):
    return n*(n+1)*(2*n+1)//6

print(sum_m(10))
print(sum_m(100))
