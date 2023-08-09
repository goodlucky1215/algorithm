import sys
from typing import List

input = sys.stdin.readline

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        answer = []
        def bfs(start:int,end:int,s:int):
            if s==k:
                result.append(answer[:])
                return
            for i in range(start,end):
                answer.append(i)
                bfs(i+1,end,s+1)
                answer.pop()

        bfs(1,n+1,0)
        return  result

print(Solution().combine(4,2))