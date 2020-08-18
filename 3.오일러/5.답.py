p=1
n=1
# 20= 1, 2, 4, 5, 10, 20
# 19, 17, 13, 11
# 18= 3, 6, 9
# 16=2,4,8
# 15 =3, 5
# 14 =2, 7
# 12 = 2,3,4,6

while True:
    if p%20 == 0 and p%19 == 0 and p%18 == 0 and p%17 == 0 and p%16 == 0 and p%15 == 0 and p%14 == 0 and p%13 == 0 and p%12 == 0 and p%11 == 0 :
        print("1~20까지 숫자로 나눠지는 가장 작은 양수는", p)
        break
    elif p%20 != 0 or p%19 != 0 or p%18 != 0 or p%17 != 0 or p%16 != 0 or p%15 != 0 or p%14 != 0 or p%13 != 0 or p%12 != 0 or p%11 != 0 :
        p += 1
        




print(p)
