#최댓갑을 구하는 알고리즘
def find_max(a):
    n=len(a)
    max_v=a[0]
    for i in range(1,n):
        if max_v<a[i]:
            max_v=a[i]
    return max_v

v=[17,92,14,33,54,7,33,42]
print(find_max(v))

#최대값의 위치를 구하는 알고리즘
def find_where_max(a):
    n=len(a)
    max_w=0
    for i in range(1,n):
        if a[max_w]<a[i]:
            max_w=i
    return max_w

print(find_where_max(v))

#최솟값을 구하는 알고리즘
def find_mini(a):
    n=len(a)
    mini_v=a[0]
    for i in range(1,n):
        if mini_v>a[i]:
            mini_v=a[i]
    return mini_v

print(find_mini(v))
