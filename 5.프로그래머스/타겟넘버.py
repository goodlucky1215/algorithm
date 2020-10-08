answer = 0
def find(k,n,le,numbers,target):
    global answer
    if k==le-1:
        if n==target:
            answer+=1
        return
    find(k+1,n+numbers[k+1],le,numbers,target)
    find(k+1,n-numbers[k+1],le,numbers,target)
    
def solution(numbers, target):
    le=len(numbers)
    find(0,numbers[0],le,numbers, target)
    find(0,-numbers[0],le,numbers, target)
    return answer
