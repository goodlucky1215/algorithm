#퀵 정렬:기준과 비교 후, 재귀 호출 -easy version
def quick_sort(a):
    n=len(a)
    if n<=1:
        return a
    g1=[]
    g2=[]
    for i in range(n-1):
        if a[n-1]>a[i]:
            g1.append(a[i])
        elif a[n-1]<a[i]:
            g2.append(a[i])
    return quick_sort(g1)+[a[n-1]]+quick_sort(g2)

d=[3,4,7,6,8,1,9,2,10,5]
print(quick_sort(d))

#퀵 정렬:기준과 비교 후, 재귀 호출 -original version
def quick_sort_sub(a,start,end):
    if end-start<=0:
        return
    pivot = a[end]
    i = start
    for j in range(start, end):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i +=1
    a[i], a[end] = a[end], a[i]
    quick_sort_sub(a, start, i-1)
    quick_sort_sub(a, i + 1, end)

def quick_sort(a):
    quick_sort_sub(a,0,len(a)-1)


d=[3,4,7,6,8,1,9,2,10,5]
quick_sort(d)
print(d)

#거품 정렬
def bubble_sort(a):
    n=len(a)
    while True:
         changed=False
         for j in range(n-1):
            if a[j]>a[j+1]:
               a[j],a[j+1]=a[j+1],a[j]
               changed=True
         if changed ==False:
               return

d=[3,4,7,6,8,1,9,2,10,5]
bubble_sort(d)
print(d)
