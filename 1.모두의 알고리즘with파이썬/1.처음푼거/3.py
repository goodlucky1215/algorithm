def same_name(a):
    n = len(a)
    result = set()
    for i in range(0,n-1):
        for  j in range(i+1,n):
            if a[i]==a[j]:
                result.add(a[i])
    return result

name=['tom','jiny','jiny','mike','tom']
print(same_name(name))
