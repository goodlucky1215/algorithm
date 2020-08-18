#최대공약수를 구하는 알고리즘
def gcd(a,b):
    i=min(a,b)
    while True:
        if a%i==0 and b%i==0:
            return i
        i-=1
        
print(gcd(3,6))      
print(gcd(60,24))

#최대공약수를 구하는 알고리즘: 유클리드 방법(재귀호출)
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

print(gcd(3,6))      
print(gcd(24,60))

#피보나치 수열 : 재귀 호출
def fivo(a,b,c):
    if c==0:
        return a
    return fivo(b,a+b,c-1)

print(fivo(0,1,5))
print(fivo(0,1,7))
    
    
def fibo(n):
    if n<=1:
        return n
    return fibo(n-2)+fibo(n-1)

print(fibo(5))
print(fibo(7))
