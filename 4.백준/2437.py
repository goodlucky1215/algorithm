n = int(input())
a = sorted(list(map(int, input().split())))

f=a[0]
for i in a:
    while i <= f:
        f+=i
        break

if a[0]!=1:
    print(1)
else:
    print(f)
    
