import collections
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        check = collections.defaultdict(list)
        for i in prerequisites:
            check[i[0]].append(i[1])

        traced = set()

        def dfs(start : int):
            if start in traced:
                return False
            traced.add(start)

            for y in check[start]:
                if not dfs(y):
                    return False
                traced.remove(i)

                return True

        for i in check:
            if not dfs(i):
                return False

        return True

print(Solution().canFinish(2,[[1,0],[0,1],[10,2]]))