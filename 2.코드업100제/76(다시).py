a=input()
i=[]
while ord(a)>96:
    i.append(a)
    a = ord(a)
    a-=1
    a = chr(a)

for k in i[::-1]:
    print(k, end=' ')

a=input()
i=ord('a')
while ord(a)<=i:
    print(chr(i), end=' ')
    i -=1
    

a=input()
b=97
while b != ord(a)+1:
    print(chr(b), end=" ")
    b+=1
