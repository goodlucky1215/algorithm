a=input().split('-')
b=0
c=0
for i in range(len(a)):
    a[i]=a[i].split('+')

for i in range(len(a[0])):
    b+=int(a[0][i])

for i in range(len(a)):
    for j in range(len(a[i])):
        c+=int(a[i][j])

print(b*2-c)
