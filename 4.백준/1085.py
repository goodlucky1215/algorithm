x,y,w,h=map(int,input().split())
p=[]
p.append(x)
p.append(y)
p.append(w-x)
p.append(h-y)
print(min(p))
