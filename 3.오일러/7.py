a=2
d=0

while d<100:
    b=[a%c for c in range(1,a+1)]
    if b[1:a-1] == 0:
        a += 1
    else:
        d=a
        a += 1

print(d)

