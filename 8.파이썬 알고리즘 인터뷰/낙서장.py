import collections
import queue
from typing import List
import collections
import re

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
head = ListNode(0)
#추가 : 선언한 head를 이동하지 않고, 주소를 참소해서 다음 노드를 추가한다.
add_node = head
add_node.next = ListNode(1)
node = head
while node:
    print(node.val)
    node = node.next



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