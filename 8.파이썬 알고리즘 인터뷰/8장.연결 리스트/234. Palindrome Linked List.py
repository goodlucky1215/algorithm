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


#deque이용
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

#런너기법
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q = None
        fast_runner = slow_runner = head

        while fast_runner and fast_runner.next:
            fast_runner = fast_runner.next.next
            q, q.next, slow_runner = slow_runner, q, slow_runner.next

        #홀수일 경우 가운데 제외해야해서, slow_runner 1칸 더 이동시킨다.
        if fast_runner:
            slow_runner = slow_runner.next

        while slow_runner and slow_runner.val==q.val:
            slow_runner, q = slow_runner.next, q.next

        return q is None # == return not q