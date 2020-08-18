i=[1,2]

p=0
n=0
s=2
while p<4000000:
	p=i[0+n]+i[1+n]
	if p<4000000 and p%2==0:
	  i.append(p)
	  n +=1
	  s=p+s
	elif p<4000000 :
	  i.append(p)
	  n +=1

print(i)
print(s)

	
