n, m = map(int,input().split())
a = list(map(int,input().split()))
result = 0 #결과
su = 0 #합
first = 0 #맨 앞 인덱스
for index,value in enumerate(a):
    su+=value
    while su > m :
        su -= a[first]
        first+=1
    while su == m :
        result+=1
        su -= a[first]
        first += 1
print(result)


