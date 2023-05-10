from typing import List

#공간복잡도가 O(1) 제한
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1] # => 같은 주소에 값을 변경
        #s = s[::-1] # => 에러, 공간을 또 따로 생성하기 때문이다

#투 포인터
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s)-1
        while(left<right):
            s[left],s[right] = s[right],s[left]
            left+=1
            right-=1

#list의 메소드
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
