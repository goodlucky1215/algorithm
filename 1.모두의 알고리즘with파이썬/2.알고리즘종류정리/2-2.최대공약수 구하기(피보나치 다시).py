#최대공약수
def gcd(a,b):
    i = min(a,b)
    while True:
        if a%i==0 and b%i==0:
            return i
        i = i - 1

print(gcd(3,6))
print(gcd(60,24))
print(gcd(81,27))

#유클리드 알고리즘 ***공식***
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b) # 좀 더 작은 값으로 자기 자신을 호출

print(gcd(3,6))
print(gcd(60,24))
#gcd(60,24)
#  ---->gcd(14,12)
#         ---->gcd(12,0)
#                     ---->12     
print(gcd(81,27))


#5-1 피보나치수열 수 구하기-재귀함수 이용 ***다시***

#내가 푼것 
def pivo(n,a,b):
    if n==1:
        return b
    return pivo(n-1,a+b,a)
print(pivo(6,1,1))

#이게 더 정
def fibo(n):
    if n<=1:
        return n
    return fibo(n-2)+fibo(n-1)
print(fibo(7))
