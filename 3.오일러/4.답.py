g=999
c=999
a=g*c
a=str(a)

while True:
    if a[0]==a[5] and a[1]==a[4] and a[2]==a[3]:
     print("100의 자리 두 숫자는",g, "와", c, "값은", a)
     break
    else:
        c -= 1
        a= g*c
        a=str(a)
        if c==990:
            c=999
            g -=1
            a= g*c
            a=str(a)



#ax([x*y for x in range(900,1000) for y in range(900,1000) if str(x*y) == str(x*y)[::-1]])



