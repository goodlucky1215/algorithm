#삽입정렬: 작은 순서대로 정리할 때,
#          앞에서부터 하나씩 꺼내서 넣은 다음에
#          다음 넣은 녀석을 삽입 시켜서 알맞은 순서에 넣는다.

#쉽게 설명한 삽입 정렬 알고리즘
def find_ins_idx(r,v):
    for i in range(0, len(r)):
            if r[i]>v:
                return i
    return len(r)

def ins_sort(a):
    result = []
    while a:
        value = a.pop(0)
        ins_idx=find_ins_idx(result, value)
        result.insert(ins_idx, value)
    return result

d=[2,4,5,1,3]
print(ins_sort(d))

#일반적인 삽입 정렬 알고리즘
def ins_sort(a):
    n = len(a)
    for i in range(1,n):
        key = a[i]
        j=i-1
        while j >=0 and a[j]>key: #while문을 다 돌때까지는 a[j+1]=key으로 아예안옴.
            a[j+1] = a[j]         #key=a[3]=4 / a[3]=a[2]=5
            j -=1                 #j=1 이됨.
        a[j+1]=key              #a[2]=key=4

        
d=[2,4,5,1,3]
ins_sort(d)
print(d)

def ins_sort(a):
    n = len(a)
    for i in range(1,n):
        key=a[i]
        j=i-1
        while j>=0 and a[j]<key:
            a[j+1]=a[j]
            j -=1
        a[j+1]=key

d=[3,4,2,1,5]
ins_sort(d)
print(d)
