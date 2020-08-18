#거품 정렬:앞뒤로 이웃한 자료를 비교


#내가 만든 거
def bubble(a,n):
    for i in range(n-1):
        if a[i]>=a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]

def bubble_sort(a,i):
    while len(a)-i>=1:
        bubble(a,len(a)-i)
        print(d)
        i += 1

d=[3,2,4,5,1,3]
bubble_sort(d,0)
print("")
print(d)
print("")

#정답
def bubble_sort(a):
    n = len(a)
    while True:
        changed = False
        for i in range(0, n-1):
            if a[i]>a[i+1]:
                print(a)
                a[i],a[i+1]=a[i+1],a[i]
                changed=True
        if changed == False:
            return
d=[3,2,4,5,1,3]
bubble_sort(d)
print(d)
