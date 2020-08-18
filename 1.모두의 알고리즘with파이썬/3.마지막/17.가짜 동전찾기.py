#앞에서부터 하나씩 비교
def coin(a,b,c,d):
    fake=29

    if a<=fake and b>= fake:
        return -1
    if c<=fake and d>= fake:
        return 1
    return 0

def find_fakecoin(left, right):
    for i in range(left+1,right+1):
       result =coin(left,left,i,i)
       if result==-1:
           return left
       elif result==1:
           return i

    return 0

n=100
print(find_fakecoin(0,n-1))

#반반 나눠서 비교
def coin(a,b,c,d):
    fake=29

    if a<=fake and b>= fake:
        return -1
    if c<=fake and d>= fake:
        return 1
    return 0

def find_fakecoin(left,right):
    if left==right:
        return left
    n=(right-left+1)//2
    left1=left
    left2=n+left-1
    right1=n+left
    right2=right1+n-1
    result = coin(left1,left2,right1,right2)
    if result ==-1:
           return find_fakecoin(left1,left2)
    elif result ==1:
           return find_fakecoin(right1,right2)
    else:
            return right

n=100
print(find_fakecoin(1,n))
