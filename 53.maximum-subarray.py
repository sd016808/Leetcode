#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        @cache
        def dp(i: int) -> int:
            ''' Return the max sum from 0 to i'''
            if i <= 0:
                return nums[i]

            return max(nums[i] + dp(i - 1), nums[i])
        
        return max(dp(i) for i in range(0, len(nums)))
# @lc code=end

