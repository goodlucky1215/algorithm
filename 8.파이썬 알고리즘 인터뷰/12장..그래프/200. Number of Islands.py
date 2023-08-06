from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid),len(grid[0])

        def dfs(i,j):
            if 0<=i<n and 0<=j<m and grid[i][j]==1:
                grid[i][j]=0
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)

        result = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    dfs(i,j)
                    result+=1

        return  result
