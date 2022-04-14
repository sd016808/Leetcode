#
# @lc app=leetcode id=1260 lang=python3
#
# [1260] Shift 2D Grid
#

# @lc code=start
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        newGrid = [x[:] for x in grid]
        flat_list = [item for sublist in grid for item in sublist]
        k = k % len(flat_list)
        for j in range(len(grid)):
            for i in range(len(grid[0])):
                newGrid[j][i] = flat_list[i+j*len(grid[0]) - k]
        
        return newGrid
# @lc code=end

