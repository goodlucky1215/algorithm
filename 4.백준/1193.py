a=int(input())
b=1
c=1
while a>b:
    a-=b
    c+=1
    b+=1
if c%2==0:
    print('%d/%d'%(a,c-(a-1)))
elif c%2==1:
    print('%d/%d'%(c-(a-1),a))
