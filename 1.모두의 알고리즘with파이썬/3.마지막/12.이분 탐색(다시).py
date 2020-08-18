#이분 탐색 알고리즘
def binary_search(a,x):
    start=0
    end=len(a)-1

    while start<=end:
        mid=(start+end)//2
        if x==a[mid]:
            return mid
        elif x> a[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1

d=[1,4,8,16,25,36,49,63,81]
print(binary_search(d,25))
print(binary_search(d,81))
print(binary_search(d,50))
d=[3]
print(binary_search(d,3))
print("")
#이분 탐색 알고리즘 - 재귀 호출
def binary(a,x,start,end):
    if end<start and a[end]!=x:
        return -1

    mid=(start+end)//2
    if a[mid]>x:
        return binary(a,x,start,mid)
    elif a[mid]<x:
        return binary(a,x,mid,end)
    else:
        return mid
    
    return -1

def binary_search(a,x):
    binary(a,x,0,len(a))

d=[1,4,8,16,25,36,49,63,81]
print(binary_search(d,25))
print(binary_search(d,81))
print(binary_search(d,50))
d=[3]
print(binary_search(d,3))
