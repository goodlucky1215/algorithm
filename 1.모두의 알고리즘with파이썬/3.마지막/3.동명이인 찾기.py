#동명이인을 찾는 알고리즘
def find_same_name(a):
    s=set()
    n=len(a)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if a[i]==a[j]:
                s.add(a[i])
    return s

name = ['tom','jery','mike','tom']
print(find_same_name(name))
name = ['tom','jery','mike','tom','jery']
print(find_same_name(name))

#짝을 지을 수 있는 조합
def make_partner(a):
    n=len(a)
    for i in range(0,n-1):
        for j in range(i+1,n):
            print(a[i],'-',a[j])

name = ['tom','jery','mike']
print(make_partner(name))
print()
name = ['tom','jery','mike','tom','jery']
print(make_partner(name))
