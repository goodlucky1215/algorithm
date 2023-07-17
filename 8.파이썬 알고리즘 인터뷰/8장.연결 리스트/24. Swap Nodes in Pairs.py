# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = head
        while root and root.next :
            root.val, root.next.val = root.next.val, root.val
            root = root.next.next
        return head

#반복
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        while prev and prev.next:
            a, b = prev, prev.next
            a.next = None
            c, b = b, b.next
            c.next = None
            a.next = b
            c.next = a
            prev = prev.next.next
        return head

#재귀
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        while head and head.next :
            a = head.next
            head.next = a.next
            head.next = self.swapPairs(head.next)
            a.next = head
            return a
        return head
