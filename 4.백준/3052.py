a=[]
for i in range(10):
    b=int(input())%42
    if b not in a:
        a.append(b)
print(len(a))