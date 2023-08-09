import sys
from typing import List

input = sys.stdin.readline

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = set()
        answer = []
        def dfs():
            answer_sum = sum(answer[:])
            if answer_sum>target :
                return
            elif answer_sum==target:
                result.add(tuple(sorted(answer)))
                return

            for i in candidates:
                answer.append(i)
                dfs()
                answer.pop()

        dfs()
        return list(map(list,result))

    def combinationSum1(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        answer = []
        end = len(candidates)
        def dfs(start:int):
            answer_sum = sum(answer[:])
            if answer_sum>target :
                return
            elif answer_sum==target:
                result.append(answer[:])
                return

            for i in range(start,end):
                answer.append(candidates[i])
                dfs(i)
                answer.pop()

        dfs(0)
        return result
print(Solution().combinationSum1([2,3,6,7], 7))