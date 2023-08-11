from typing import List
import sys
input = sys.stdin.readline

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2' : 'abc', '3' : 'def', '4' : 'ghi' ,
                 '5' : 'jkl', '6' : 'mno', '7' : 'pqrs',
                 '8' : 'tuv', '9' : 'wxyz'}
        result = []
        if digits=="":
            return result

        def phone_combination(start, end, letter):
            if start==end:
                result.append(letter)
                return

            for i in phone[digits[start]]:
                phone_combination(start+1,end,letter+i)

        phone_combination(0, len(digits), "")
        return result





digits = input().strip()
print(Solution().letterCombinations(digits))