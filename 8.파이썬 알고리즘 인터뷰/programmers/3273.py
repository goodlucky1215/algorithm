n = int(input())
a = list(map(int,input().split()))
x = int(input())
a.sort()

def find_result():
    if n==1 :
        return 0
    left,right=0,1
    for i in a:
        if a[left]+a[right]>x:
        elif a[left]+a[right]<x:
            right+=1



print(find_result())