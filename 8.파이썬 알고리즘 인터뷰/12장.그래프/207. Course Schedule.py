from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        check = []
        for i in range(numCourses+1):
            check.append([0]*(numCourses+1))

        for i in prerequisites:
            if check[i[0]][i[1]]==1 or i[0]==i[1] :
                return False
            check[i[0]][i[1]]=1
            check[i[1]][i[0]]=1
        return True