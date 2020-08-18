def couple(a):
    n=len(a)
    for i in range(n-1):
        for  j in range(i+1,n):
            print(name[i],'-',name[j])


name=['tom','jerry','mike']

print(couple(name))
