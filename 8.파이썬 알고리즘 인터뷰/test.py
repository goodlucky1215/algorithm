#1-1 : 루프
sum = 0
for i in range(1,10+1):
    sum +=i
print("sum : ", sum);

#1-2 : 루프
#sum = sum(i for i in range(1,10+1))
#print("sum : ", sum);

#1-3 : 루프
sum = 0
sum = sum(range(1,10+1))
print("sum : ", sum);