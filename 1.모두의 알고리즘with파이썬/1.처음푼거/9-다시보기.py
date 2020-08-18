def find_where(r,v):
    for i in range(0,len(r)):
        if v<r[i]:
            return i
    return len(r) #v가 모든 r보다 클경우 가장 끝에 들어가므로 길이len(r)과 같음.
def ins_sort(a):
    result=[]
    while a:
        value = a.pop(0)
        ins_idx=find_where(result,value)
        result.insert(ins_idx, value)
    return result

d=[2, 4, 5, 1, 3]
print(ins_sort(d))

def ins_sort(a):
    n = len(a)
    for i in range(1,n):
        key=a[i]
        j= i-1
        while j>=0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key

d=[2,4,5,1,3]
ins_sort(d)
print(d)
