#퀵정렬 :병합 정렬과 같이 그룹을 둘로 나눈 점은 같다.
#        but!!!!!!!그룹을 나눌 때, '미리 기준을 잡고' 그와 비교해서 나눈다.

#쉽게 설명한 퀵 정렬 알고리즘
def quick_sort(a):
    n = len(a)
    if n<= 1:
        return a
    pivot = a[-1]
    g1 = []
    g2 = []
    for i in range(0,n-1):
        if a[i] < pivot:
            g1.append(a[i])
        else:
            g2.append(a[i])
    return quick_sort(g1)+[pivot]+quick_sort(g2)

d=[6,8,3,9,10,1,2,4,7,5]
print(quick_sort(d))

#일반적인 퀵 알고리즘 ******이게 진짜 어려움@@
def quick_sort_sub(a, start, end):
    if end-start<=0:
        return
    pivot = a[end]
    i = start
    for j in range(start,end):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i],a[end]=a[end],a[i]
    quick_sort_sub(a,start,i-1)
    quick_sort_sub(a, i+1, end)

def quick_sort(a):
    quick_sort_sub(a,0,len(a)-1)

d=[6,8,3,9,10,1,2,4,7,5]
quick_sort(d)
print(d)
