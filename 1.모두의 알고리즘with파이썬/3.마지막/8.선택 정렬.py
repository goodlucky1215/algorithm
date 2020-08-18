#선택 정렬로 세우기: easy version
def find_min_idx(a):
    n=len(a)
    m=0
    for i in range(1,n):
        if a[m]>a[i]:
            m=i
    return m

def sel_sort(a):
    s=[]
    while a:
        m=find_min_idx(a)
        value=a.pop(m)
        s.append(value)
    return s

v=[2,4,5,1,3]
print(sel_sort(v))

#선택 정렬로 세우기: original version -작은 수에서 큰 수로
def sel_sort(a):
    n=len(a)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]

v=[2,4,5,1,3]
sel_sort(v)
print(v)

#선택 정렬로 세우기: original version -큰 수에서 작은 수로
def sel_sort(a):
    n=len(a)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if a[i]<a[j]:
                a[i],a[j]=a[j],a[i]

v=[2,4,5,1,3]
sel_sort(v)
print(v)                
