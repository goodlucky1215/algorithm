N=int(input())
tip=[]
result=0
for i in range(N):
    tip.append(int(input()))
tip.sort(reverse=True)
for i in range(N):
    if tip[i]-(i+1-1)>0:
        result+=tip[i]-(i+1-1)
print(result)
