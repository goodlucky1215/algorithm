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

    def canFinish1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        check = collections.defaultdict(list)
        for i in prerequisites:
            check[i[0]].append(i[1])

        traced = set()
        finish = set()

        def dfs(start : int):
            if start in traced:
                return False

            if start in finish:
                return True

            traced.add(start)

            for i in check[start]:
                if dfs(i)==False:
                    return False

            traced.remove(start)
            finish.add(start)
            return True

        for i in list(check):
            if not dfs(i):
                return False

        return True


print(Solution().canFinish1(5,[[1,4],[2,4],[3,1],[3,2]]))