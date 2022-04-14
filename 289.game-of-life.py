#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#

# @lc code=start
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def count_neighbors(i, j):
            count = 0
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if x == i and y == j:
                        continue
                    if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                        continue
                    if board[x][y] & 1 == 1:
                        count += 1
            return count
  
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                count = count_neighbors(i, j)
                if board[i][j] == 1:
                    if count >= 2 and count <= 3:
                        board[i][j] += 2
                else:
                    if count == 3:
                        board[i][j] += 4

        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] >= 3:   
                    board[i][j] = 1
                else:
                    board[i][j] = 0

# @lc code=end

