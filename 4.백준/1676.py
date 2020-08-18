n=int(input())
c=1
d=0
for i in range(1,n+1):
    c*=i
c=str(round(c))
for i in c[::-1]:
    if i=='0':
        d+=1
    else:
        break
print(d)
