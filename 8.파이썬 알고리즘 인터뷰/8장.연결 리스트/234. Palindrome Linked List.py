import collections
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q: List = []

        if not head:
            return True

        node = head

        while node:
            q.append(node.val)
            node =node.next

        while len(q)>1:
            if q.pop(0)!=q.pop():
                return False
        return True

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q = collections.deque()

        if not head:
            return True

        node = head

        while node:
            q.append(node.val)
            node =node.next

        while len(q)>1:
            if q.popleft()!=q.pop():
                return False
        return True