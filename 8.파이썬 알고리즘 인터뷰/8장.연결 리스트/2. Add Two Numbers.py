# Definition for singly-linked list.
from typing import Optional
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = 0
        su = 1
        while l1 or l2:
            if l1:
                result+=(l1.val*su)
                l1 = l1.next
            if l2:
                result+=(l2.val*su)
                l2 = l2.next
            su*=10
        nodeResult = ListNode(result%10)
        result //= 10
        head = nodeResult
        while result>0:
           nodeResult.next = ListNode(result%10)
           nodeResult = nodeResult.next
           result //= 10
        return head

