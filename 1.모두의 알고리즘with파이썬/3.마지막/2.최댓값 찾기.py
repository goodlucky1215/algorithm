#최댓값 찾기
def find_max(a):
    m=a[0]
    for i in a:
        if i>m:
            m=i
    return m

v=[17,92,18,33,58,7,33,42]
print(find_max(v))

#최댓값 위치 찾기
def find_max(a):
    m=0
    for i in range(len(a)):
        if a[i]> a[m]:
            m=i
    return m

v=[17,92,18,33,58,7,33,42]
print(find_max(v))

#최솟값 찾기
def find_min(a):
    m=a[0]
    for i in a:
        if i<m:
            m=i
    return m

v=[17,92,18,33,58,7,33,42]
print(find_min(v))

#최솟값 위치 찾기
def find_min(a):
    m=0
    for i in range(len(a)):
        if a[i]<a[0]:
            m=i
    return m

v=[17,92,18,33,58,7,33,42]
print(find_min(v))
