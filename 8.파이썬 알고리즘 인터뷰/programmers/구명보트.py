import sys
input = sys.stdin.readline

def solution(people, limit):
    people.sort()
    left, right = 0, len(people)-1
    result = 0
    while left<right:
        if people[left]+people[right]<=limit:
            left+=1
        result+1
        right-=1


