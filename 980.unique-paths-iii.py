# You are given an m x n integer array grid where grid[i][j] could be:

# 1 representing the starting square. There is exactly one starting square.
# 2 representing the ending square. There is exactly one ending square.
# 0 representing empty squares we can walk over.
# -1 representing obstacles that we cannot walk over.

from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.ans = 0
        m = len(grid)
        n = len(grid[0])
        self.steps = 1
        self.totalSteps = 0
        def backTracking(i, j):
            if grid[i][j] >= 1:
                if self.steps == self.totalSteps:
                    self.ans += 1
                else:
                    return

            if i - 1 >= 0 and grid[i - 1][j] >= 0:
                self.steps += 1
                grid[i - 1][j] -= 1
                backTracking(i - 1, j)
                grid[i - 1][j] += 1
                self.steps -= 1
            if i + 1 < m and grid[i + 1][j] >= 0:
                self.steps += 1
                grid[i + 1][j] -= 1
                backTracking(i + 1, j)
                grid[i + 1][j] += 1
                self.steps -= 1
            if j - 1 >= 0 and grid[i][j - 1] >= 0:
                self.steps += 1
                grid[i][j - 1] -= 1
                backTracking(i, j - 1)
                grid[i][j - 1] += 1
                self.steps -= 1
            if j + 1 < n and grid[i][j + 1] >= 0:
                self.steps += 1
                grid[i][j + 1] -= 1
                backTracking(i, j + 1)
                grid[i][j + 1] += 1
                self.steps -= 1
        
        start_i = None
        start_j = None
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] >= 0:
                    self.totalSteps += 1
                    if grid[i][j] == 1:
                        start_i = i
                        start_j = j
        
        grid[start_i][start_j] = -1
        backTracking(start_i, start_j)
        return self.ans

print(Solution().uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))