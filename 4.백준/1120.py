a,b=map(str, input().split(' '))
c=0
d=0
e=[]

for i in range(len(b)-len(a)+1):
        for j in range(len(a)):
            if a[j]!=b[j+c]:
                d+=1
        e.append(d)
        d=0
        c+=1

print(min(e))
