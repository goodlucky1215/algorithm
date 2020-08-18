a=input()
b=[-1]*26
for i in range(len(a)):
    if b[ord(a[i])-97]==-1:
        b[ord(a[i])-97]=i
print(*b)
