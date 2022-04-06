#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''Log(M*N) = Log(M) + Log(N) 故這題其實用一次二元搜尋即可'''
        if matrix[0][0] > target or matrix[-1][-1] < target:
            return False
        
        col_0 = [row[0] for row in matrix]
        rowIndx = self.binarySearch1(col_0, target)
        return self.binarySearch2(matrix[rowIndx], target)
    
    def binarySearch1(self, l: List[int], target) -> int:
        left = 0
        right = len(l) - 1
        while left <= right:
            mid = (left + right) // 2
            if l[mid] == target:
                return mid
            elif l[mid] < target:
                left = mid + 1
            else:
                right = mid - 1 
        
        if l[mid] < target:
            return mid
        else:
            return mid - 1
    
    def binarySearch2(self, l: List[int], target) -> int:
        left = 0
        right = len(l) - 1
        while left <= right:
            mid = (left + right) // 2
            if l[mid] == target:
                return True
            elif l[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
        

# @lc code=end

