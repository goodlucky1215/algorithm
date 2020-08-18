def func(n):
    if n==0:
        return 0
    return n+func(n-1)

print(func(3))


def func(n,max_n):
    s=n.pop(0)
    if max_n<s:
        max_n=s
    while n:
        return func(n,max_n)
    return max_n

a=[12,45,2,4,3,6,23,63,13,8]
print(func(a,0))


#이게 좀 헷갈
def find_max(a,n):
    if n==1:
        return a[0]
    max_n_1 = find_max(a,n-1)
    if max_n_1 > a[n-1]:
        return max_n_1
    else:
        return a[n-1]

a=[12,45,2,4,3,6,23,63,13,8]
print(func(a,len(a)))
