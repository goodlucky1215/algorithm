#병렬 정렬로 세우기: easy version - 재귀 호출
def merge_sort(a):
    n=len(a)
    if n<=1:
        return a
    mid=n//2
    g1=merge_sort(a[:mid])
    g2=merge_sort(a[mid:])
    result=[]
    while g1 and g2:
        if g1[0]<g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))
    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
    return result

d=[3,4,7,6,8,1,9,5,10,2]
print(merge_sort(d))
    
#병렬 정렬로 세우기: original version -작은 수에서 큰 수로
def merge_sort(a):
    n=len(a)
    if n<=1:
        return
    mid=n//2
    g1=a[:mid]
    g2=a[mid:]
    merge_sort(g1)
    merge_sort(g2)
    i1=0
    i2=0
    ia=0
    while i1 < len(g1) and i2 < len(g2):
        if g1[i1]<g2[i2]:
            a[ia]=g1[i1]
            ia+=1
            i1+=1
        else:
            a[ia]=g2[i2]
            ia+=1
            i2+=1
    while i1<len(g1):
        a[ia]=g1[i1]
        ia+=1
        i1+=1
    while i2<len(g2):
        a[ia]=g2[i2]
        ia+=1
        i2+=1

d=[3,4,7,6,8,1,9,5,10,2]
merge_sort(d)
print(d)

#병렬 정렬로 세우기: original version -큰 수에서 작은 수로
def merge_sort(a):
    n=len(a)
    if n<=1:
        return
    mid=n//2
    g1=a[:mid]
    g2=a[mid:]
    merge_sort(g1)
    merge_sort(g2)
    i1=0
    i2=0
    ia=0
    while i1<len(g1) and i2<len(g2):
        if g1[i1]>g2[i2]:
            a[ia]=g1[i1]
            ia +=1
            i1 +=1
        else:
            a[ia]=g2[i2]
            ia +=1
            i2 +=1
    while i1<len(g1):
        a[ia]=g1[i1]
        ia +=1
        i1 +=1
    while i2<len(g2):
        a[ia]=g2[i2]
        ia +=1
        i2 +=1

d=[3,4,7,6,8,1,9,5,10,2]
merge_sort(d)
print(d)
        
