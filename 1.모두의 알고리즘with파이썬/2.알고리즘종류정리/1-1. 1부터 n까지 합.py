#방법1
def sum_n(n):
    s = 0
    for i in range(1,n+1):
        s = s+i
    return s

print(sum_n(10))
print(sum_n(100))

#방법2
def sum_n(n):
    return n*(n+1)/2

print(sum_n(10))
print(sum_n(100))
 
#예제1-1
def app_n(n):
    s=0
    for i in range(1,n+1):
        s += i*i
    return s

print(app_n(10))
print(app_n(100))

#예제1-3
def app_n(n):
    return n*(n+1)*(2*n+1)/6

print(app_n(10))
print(app_n(100))
