from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        
        res = [[1], [1, 1]]
        for i in range(2, numRows):
            res.append([1] + [res[i-1][j-1] + res[i-1][j] for j in range(1, len(res[i - 1]))] + [1])
        
        return res