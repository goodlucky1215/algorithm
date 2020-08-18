def choice_max(d):
    n=len(d)
    for i in range(n-1):
        for j in range(i+1,n):
            if d[i]<d[j]:
                d[i],d[j]=d[j],d[i]
d=[2,4,5,1,3]
choice_max(d)
print(d)

def find_max(d):
    max_id=0
    for i in range(1,len(d)):
        if d[max_id]<d[i]:
            max_id=i
    return max_id
def sel_sort(d):
    result=[]
    while d:
        result.append(d.pop(find_max(d)))
    return result

d=[2,4,5,1,3]
print(sel_sort(d))
