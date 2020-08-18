a=input()
time=0
for j in a:
    i=ord(j)
    if 65<=i and 67>=i:
        time+=3
    elif 68<=i and 70>=i:
        time+=4
    elif 71<=i and 73>=i:
        time+=5
    elif 74<=i and 76>=i:
        time+=6
    elif 77<=i and 79>=i:
        time+=7
    elif 80<=i and 83>=i:
        time+=8
    elif 84<=i and 86>=i:
        time+=9
    elif 87<=i and 90>=i:
        time+=10
print(time)
