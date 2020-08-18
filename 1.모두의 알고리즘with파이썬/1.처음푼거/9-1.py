def ins_sort(d):
    n = len(d)
    for i in range(1,n):
        key=d[i]
        j= i-1
        while j>=0 and d[j]>key:
            d[j+1] = d[j]
            j -= 1
        d[j+1]=key

d=[2,4,5,3,1]
ins_sort(d)
print(d)

def ins_sort(d):
    n =len(d)
    for i in range(1,n):
        key=d[i]
        j = i-1
        while j>=0 and d[j]<key:
            d[j+1] = d[j]
            j -= 1
        d[j+1]=key

d=[3,4,5,2,6,1]
ins_sort(d)
print(d)
