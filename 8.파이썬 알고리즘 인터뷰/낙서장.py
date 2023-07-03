import collections
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
class Node:
    def __init__(self, data, next=None):  #data 만 입력시 next 초기값은 None이다.
        self.data = data #다음 데이터 주소 초기값 = None
        self.next = next

s = Node(1)
head = s
s.next = Node(2)
s = s.next
s.next = Node(3)
s = s.next
s.next = Node(4)
s = s.next
while head:
    if head:
        head.next
        print(head.data)

#while head :
print(head.data)
print(head.next.data)
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