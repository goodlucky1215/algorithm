#기본적인 정렬의 종류는 5가지
#선택 정렬/ 삽입 정렬/ 병합 정렬/ 퀵 정렬/ 거품 정렬

#선택 정렬-학생들을 일렬로 세우고 그 중 키가 작은 애를 뽑아 골라서 세움.
def find_min_idx(a):
    n = len(a)
    min_idx = 0
    for i in range(1,n):
        if a[i] < a[min_idx]:
            min_idx= i
    return min_idx

def sel_sort(a):
    result = []
    while a:
        min_idx = find_min_idx(a)
        value = a.pop(min_idx)
        result.append(value)
    return result

d=[2,4,5,1,3]
print(sel_sort(d))

#일반적인 선택 알고리즘
def sel_sort(a):
    n = len(a)
    for i in range(0,n-1):
        for j in range(i + 1, n):
            if a[j] < a[i]:
                a[i],a[j]=a[j],a[i]

d=[2,4,5,1,3]
sel_sort(d)
print(d)

def sel_sort(a):
    n=len(a)
    for i in range(n-1):
        for j in range(i+1,n):
            if a[i]<a[j]:
                a[i],a[j]=a[j],a[i]
                
d=[2,4,5,1,3]
sel_sort(d)
print(d)          
