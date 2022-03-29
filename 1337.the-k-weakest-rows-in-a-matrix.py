#
# @lc app=leetcode id=1337 lang=python3
#
# [1337] The K Weakest Rows in a Matrix
#

# @lc code=start
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        table = [[0, m] for m in range(0, len(mat))]
        for m in range(0, len(mat)):
            for n in range(0, len(mat[m])):
                if mat[m][n] == 1:
                    table[m][0] += 1
                else:
                    break
        
        table.sort(key = lambda t :t[0])
        return [t[1] for t in table[0:k]]
        

# @lc code=end

