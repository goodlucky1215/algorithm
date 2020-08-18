#이분탐색: 백과사전에서 쪽수 찾듯이, 정렬된 리스트에서 원하는 값 찾기
#          탐색할 자료를 둘로 나누어 찾는 값이 있을 법한 곳만 탐색해서
#          하나하나 찾는 순차 탐색보다 빨리 찾을 수 있음.

def binary_search(a,x):
    start=0
    end=len(a)-1

    while start<=end:
        mid=(start+end)//2
        if x == a[mid]:
            return mid
        elif x> a[mid]:
            start = mid+1
        else:
            end = mid-1

    return -1

d=[1,4,9,16,24,36,47,63,91]
print(binary_search(d,36))
print(binary_search(d,50))
        
#재귀호출 이분탐색 알고리즘
def binary_search_sub(a,x,start,end):
    if start>end:
        return -1
    
    mid=(start+end)//2
    if x == a[mid]:
        return mid
    elif x >a[mid]:
        return binary_search_sub(a,x,mid+1,end)
    else:
        return binary_search_sub(a,x,start,mid-1)
    
    return -1

def binary_search(a,x):
    return binary_search_sub(a,x,0,len(a)-1)

d=[1,4,9,16,24,36,47,63,91]
print(binary_search(d,36))
print(binary_search(d,50))
print(binary_search_sub(d,63,0,len(d)-1))
