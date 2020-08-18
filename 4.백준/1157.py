a=input()
a=a.upper()
b=[0]*26
for i in a:
    b[ord(i)-65]+=1
c=max(b)
d=[]
for i in range(len(b)):
    if b[i]==c:
        d.append(i)
if len(d)>1:
    print('?')
else:
    print(chr(d[0]+65))
