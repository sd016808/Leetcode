#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return []
        
        matrix = [[0] * n for _ in range(n)]
        i, j = 0, 0
        totalStep = n * n
        step = 1
        while step <= totalStep:
            # Go right
            while j < n and matrix[i][j] == 0:
                matrix[i][j] = step
                j += 1
                step += 1

            j -= 1
            i += 1

            # Go down
            while i < n and matrix[i][j] == 0:
                matrix[i][j] = step
                i += 1
                step += 1

            i -= 1
            j -= 1

            # Go left
            while j >= 0 and matrix[i][j] == 0:
                matrix[i][j] = step
                j -= 1
                step += 1

            j += 1
            i -= 1
            
            # Go up
            while i >= 0 and matrix[i][j] == 0:
                matrix[i][j] = step
                i -= 1
                step += 1

            i += 1
            j += 1
        
        return matrix
# @lc code=end

