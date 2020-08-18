def search_list(a,x):
    result=[]
    for i in range(len(a)):
        if a[i]==x:
            result.append(i)
    return result

a=[2,3,5,6,13,2,4,13,5,13]
print(search_list(a,13))
