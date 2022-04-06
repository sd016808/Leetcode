#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        if nums[0] == target:
            return True
        
        lastNum = nums[0]
        isFindRotated = False
        for n in nums[1:]:
            if n == target:
                return True
            
            if isFindRotated:
                if target > nums[0] or target < n:
                    return False
            
            if not isFindRotated:
                isFindRotated = n < lastNum

            lastNum = n
        
        return False


# @lc code=end

