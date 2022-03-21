#
# @lc app=leetcode id=799 lang=python3
#
# [799] Champagne Tower
#

# @lc code=start
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured < 1:
            return 0 if query_row > 0 or query_glass > 0 else poured
        
        tower = [[poured]] 
        row_index = 1 # zero-base
        remain = poured
        while remain > 0:
            remain = 0
            row = []
            row.append(max((tower[row_index-1][0] - 1)/2, 0))
            remain += row[-1]
            for i in range(0, len(tower[row_index-1]) - 1):
                row.append(max((tower[row_index-1][i] - 1)/2, 0) + max((tower[row_index-1][i + 1] - 1)/2, 0))
                remain += row[-1]
            row.append(max((tower[row_index-1][-1] - 1)/2, 0))
            remain += row[-1]
            tower.append(row)
            
            if row_index >= query_row:
                break

            row_index += 1
        
        try:
            return 1 if tower[query_row][query_glass] > 1 else tower[query_row][query_glass]
        except:
            return 0

# @lc code=end

