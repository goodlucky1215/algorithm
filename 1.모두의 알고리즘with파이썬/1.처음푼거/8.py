def choic_algo(a):
    b=len(a)
    for i in range(b-1):
        for j in range(i+1,b):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]

d=[2,4,5,3,1]
choic_algo(d)
print(d)

def find_min(a):
    n=len(a)
    min_id=0
    for i in range(1,n):
        if a[i]<a[min_id]:
            min_id=i
    return min_id
def sel_sort(a):
    result=[]
    while a:
        b=a.pop(find_min(a))
        result.append(b)
    return result

d=[2,4,5,3,1]
print(sel_sort(d))
