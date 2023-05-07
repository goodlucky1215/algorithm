# 처음 시도
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_isalpha = ""
        s_upper = s.upper()
        for i in range(0, len(s)):
            if (s_upper[i].isalpha() or s_upper[i].isdigit()): s_isalpha += s_upper[i]
        s_len = len(s_isalpha) - 1
        for i in range(0, len(s_isalpha) // 2):
            if (s_isalpha[i] != s_isalpha[s_len - i]): return False
        return True


# 리스트 변환
class Solution:
    def isPalindrome1(self, s: str) -> bool:
        s_list = []
        for i in s:
            if i.isalnum():
                s_list.append(i.lower())
        while len(s_list) > 1:
            if s_list.pop(0) != s_list.pop():
                return False
        return True


# 데큐 변환
import collections

class Solution:
    def isPalindrome2(self, s: str) -> bool:
        s_deque = collections.deque()
        for i in s:
            if i.isalnum():
                s_deque.append(i.lower())
        while len(s_deque) > 1:
            if s_deque.popleft() != s_deque.pop():
                return False
        return True


# 슬라이싱
import re
class Solution:
    def isPalindrome3(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9','',s)
        return s == s[::-1]
