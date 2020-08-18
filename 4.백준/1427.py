a=int(input())
b=[]
for i in str(a):
    b.append(int(i))
b.sort(reverse=True)
for i in b:
    print(i,end='')
