a=input()
p=['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in p:
    a=a.replace(i,'/',1000)
print(len(a))