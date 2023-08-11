import sys
from typing import List

sys = sys.input.readline

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        answer = []
        end = 0
        nums_l = len(nums)

        def dfs(start : int, index : int) :
            if start==end:
                result.append(answer[:])
                return

            for i in range(index,nums_l):
                answer.append(nums[i])
                dfs(start+1,i+1)
                answer.pop()

        for i in range(1,nums_l+1):
            end = i
            dfs(0, 0)

        return result
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        answer = []
        nums_l = len(nums)

        def dfs(index : int) :
            result.append(answer[:])

            for i in range(index,nums_l):
                answer.append(nums[i])
                dfs(i+1)
                answer.pop()

        dfs(0)

        return result