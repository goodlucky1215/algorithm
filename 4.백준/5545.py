n = int(input())
a,b = map(int,input().split())
c=int(input())
topping=[]
pizza_cal=c/a

for i in range(n):
   topping.append(int(input()))
                  
topping.sort(reverse=True)
                  
for i in range(1,n+1):
   if pizza_cal<(c+sum(topping[:i]))/((i)*b+a):
                  pizza_cal=(c+sum(topping[:i]))/((i)*b+a)
                  
print(int(pizza_cal))
