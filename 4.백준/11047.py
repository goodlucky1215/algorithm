a,pay=map(int,input().split())
coin=[int(input()) for i in range(a)]
d=0
n=-1

while pay!=0:
   if pay >= coin[n]:
         d+=pay//coin[n]
         pay%=coin[n]
   elif pay < coin[n]:
         n-=1
         
print(d)
