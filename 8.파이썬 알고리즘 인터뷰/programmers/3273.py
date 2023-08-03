n = int(input())
a = list(map(int,input().split()))
x = int(input())
a.sort()

def find_result():
    if n==1 :
        return 0
    result = 0
    left,right=0,n-1
    while left<right:
        if a[left]+a[right]<x:
            left+=1
        elif a[left]+a[right]>x:
            right-=1
        else:
            right -= 1
            result+=1
    return result



print(find_result())