a=1
b=600851475143
s=0

while a < 60030:
   if b%a==0 :
          b= b//a
          s=a
          a +=1
   else:
          a += 1



print(s)



 
    
