import sys
from typing import List

input = sys.stdin.readline

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums_len = len(nums)
        check = [False]*nums_len

        def bfs(answer : List[int]) :
            if len(answer)==nums_len:
                result.append(answer[:])
                return

            for index,value in enumerate(nums):
                if not check[index]:
                    check[index]=True
                    answer.append(value)
                    bfs(answer)
                    answer.pop()
                    check[index]=False

        bfs([])
        return result


print(Solution().permute([1,2,3]))