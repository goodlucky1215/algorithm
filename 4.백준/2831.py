N=int(input())
men=sorted(list(map(int,input().split())))
women=sorted(list(map(int,input().split())))
re=0
men1, men2,women1,women2=[],[],[],[]
for i in range(N):
    if men[i]<0:
        men1.append(-men[i])
    else:
        men2.append(men[i])
for i in range(N):
    if women[i]<0:
        women1.append(-women[i])
    else:
        women2.append(women[i])
k,j=0,0
while j<len(women2) and k<len(men1):
       if men1[k]>women2[-j-1]:
            re+=1
            k+=1
            j+=1
       else:
            j+=1
k,j=0,0
while j<len(men2) and k<len(women1):
       if women1[k]>men2[-j-1]:
            re+=1
            k+=1
            j+=1
       else:
            j+=1
print(re)

