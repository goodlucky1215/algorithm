#1-1 : 루프
sum1 = 0
for i in range(1,10+1):
    sum1 +=i
print("sum : ", sum1);

#1-2 : 루프
sum1 = sum(i for i in range(1,10+1))
print("sum : ", sum1);

#1-3 : 루프
sum1 = sum(range(1,10+1))
print("sum : ", sum1);