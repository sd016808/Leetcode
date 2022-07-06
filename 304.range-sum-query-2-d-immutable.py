#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#

# @lc code=start
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.dp = matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    self.dp[i][j] = self.dp[i][j] + self.dp[i][j-1]
                elif j == 0:
                    self.dp[i][j] = self.dp[i][j] + self.dp[i-1][j]
                else:
                    self.dp[i][j] = self.dp[i][j] + self.dp[i][j-1] + self.dp[i-1][j] - self.dp[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.dp[row2][col2]
        elif row1 == 0:
            return self.dp[row2][col2] - self.dp[row2][col1-1]
        elif col1 == 0:
            return self.dp[row2][col2] - self.dp[row1-1][col2]
        else:
            return self.dp[row2][col2] - self.dp[row2][col1-1] - self.dp[row1-1][col2] + self.dp[row1-1][col1-1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

