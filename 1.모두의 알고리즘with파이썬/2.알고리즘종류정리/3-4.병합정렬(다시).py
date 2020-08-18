#병합정렬: 재귀 호출을 활용한 정렬.
#줄세우기: 두 조로 나눠서 키 순서대로 안에서 정렬 시키고
#          두 조의 앞의 한 명씩 돌아가면서 비교 시켜서 줄을 세움

#쉽게 설명한 병합 정렬 알고리즘
def merge_sort(a):
    n=len(a)
    if n<= 1:
        return a
    mid = n//2
    g1 = merge_sort(a[:mid])
    g2 = merge_sort(a[mid:])
    result = []
    while g1 and g2:
        if g1[0] < g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))
    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
    return result

d=[6,8,3,9,10,1,2,4,7,5]
print(merge_sort(d))

def merge_sort(a):
    n = len(a)
    if n<= 1:
        print('erer')
        return 
    mid = n//2
    g1 = a[:mid]
    g2 = a[mid:]
    merge_sort(g1)
    merge_sort(g2)
    i1 = 0
    i2 = 0
    ia = 0
    while i1<len(g1) and i2<len(g2):
        if g1[i1] < g2[i2]:
            a[ia] = g1[i1]
            i1 += 1
            ia += 1
        else:
            a[ia] = g2[i2]
            i2 += 1
            ia += 1
    while i1 < len(g1):
        a[ia] = g1[i1]
        i1 += 1
        ia += 1
    while i2 < len(g2):
        a[ia] = g2[i2]
        i2 += 1
        ia += 1
        
d=[6,8,3,9,10,1,2,4,7,5]
merge_sort(d)
print(d)

def merge_sort(a):
    n=len(a)
    if n<=1:
        return
    mid = n//2
    g1 = a[:mid]
    g2 = a[mid:]
    merge_sort(g1)
    merge_sort(g2)
    i1 = 0
    i2 = 0
    ia = 0
    while i1<len(g1) and i2<len(g2):
        if g1[i1] < g2[i2]:
            a[ia]=g2[i2]
            i2 += 1
            ia += 1
        else:
            a[ia]=g1[i1]
            i1 += 1
            ia += 1
    while i1 < len(g1):
        a[ia] = g1[i1]
        i1 += 1
        ia += 1
    while i2 < len(g2):
        a[ia] = g2[i2]
        i2 += 1
        ia += 1
        
d=[6,8,3,9,10,1,2,4,7,5]
merge_sort(d)
print(d)

