import collections
import functools
import queue
from typing import List, Optional
import collections
import re
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''

stack = []
stack.append(1)
stack.append(2)
print(stack[-1])
a = 0
if a==0:
    print("Sdfsdfeeeeeeee")
for i in range(1):
    print(i)
class Node:
    def __init__(self, data, next=None):  #data 만 입력시 next 초기값은 None이다.
        self.data = data #다음 데이터 주소 초기값 = None
        self.next = next

result = []
table = {
        ")" : "(",
        "]" : "[",
        "}" : "{"
}

if not result:
    print("빈값")


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
lists = ['ad','cx','da']
di = {}
for i, j in enumerate(lists):
    di[j] = i
for s in di:
    if 'ad' in di :
        print("sdfsdfsd")
result = set()

lists= [1, 2, 3]
lists.sort()

result.add(tuple(lists))
result.add(tuple([1, 2, 3]))
print(result)
result_list = [list(t) for t in result]
print(result_list)

a = [1,2,3,4,5]
int(''.join(map(str,a)))

print(functools.reduce(lambda x,y:x*10+y,a,0))