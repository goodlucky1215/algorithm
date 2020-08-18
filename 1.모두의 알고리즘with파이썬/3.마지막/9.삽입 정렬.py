#삽입 정렬로 세우기: easy version
def find_ins_idx(r,v):
    for i in range(0, len(r)):
        if v < r[i]:
            return i
    return len(r)

def ins_sort(a):
    s=[]
    while a:
        value=a.pop(0)
        m=find_ins_idx(s,value)
        s.insert(m,value)
    return s

v=[2,4,5,1,3]
print(ins_sort(v))

#삽입 정렬로 세우기: original version -작은 수에서 큰 수로
def ins_sort(a):
    for i in range(1,len(a)):
        key=a[i]
        j=i-1
        while j>=0 and a[j]>key:
            a[j+1]=a[j]
            j -= 1
        a[j+1]=key


v=[3,4,1,2,5]
ins_sort(v)
print(v)

#삽입 정렬로 세우기: original version -큰 수에서 작은 수로
def int_sort(a):
    for i in range(1,len(a)):
        key=a[i]
        j=i-1
        while j>=0 and a[j]<key:
            a[j+1]=a[j]
            j -= 1
        a[j+1]=key



v=[3,4,1,2,5]
int_sort(v)
print(v)            
            
