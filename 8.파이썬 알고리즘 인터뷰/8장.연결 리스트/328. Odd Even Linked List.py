# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = head
        a1 = a = ListNode(None)
        while head and head.next :
            a = head.next # 2 3
            a.next, b = None, a.next # a는 2 b는 3
            head.next = b # 1 3
            head = head.next # 3
            a = a.next #None
        head.next = a1.next
        return result
