n = int(input())
m=[]
for i in range(n):
    k=input()
    m.append(k)
m=list(set(m))
m.sort(key=lambda x:(len(x),x))
for i in m:
    print(i)

n = int(input())
m=[]
re=[]
for i in range(51):
    m.append([])
for i in range(n):
    k=input()
    m[len(k)].append(k)
for i in range(51):
    m[i]=list(set(m[i]))
    m[i].sort()
    if m[i] !=[]:
        for k in m[i]:
            print(k)
