#
# @lc app=leetcode id=918 lang=python3
#
# [918] Maximum Sum Circular Subarray
#

# @lc code=start
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:  
        # '''若最大值發生在循環，則為 Sum(nums) - 最小DP值'''
        # '''最最大值沒有在循環，則為最大DP值'''     
        # if max(nums) <= 0: return max(nums)
        # @cache
        # def dpMin(i: int) -> int:
        #     ''' Return the min sum from 0 to i'''
        #     if i <= 0:
        #         return nums[i]
        #     return min(nums[i] + dpMin(i - 1), nums[i])

        # @cache
        # def dpMax(i: int) -> int:
        #     ''' Return the min sum from 0 to i'''
        #     if i <= 0:
        #         return nums[i]
        #     return max(nums[i] + dpMax(i - 1), nums[i])
        # return max(max(dpMax(i) for i in range(0, len(nums))), sum(nums) - min(dpMin(i) for i in range(0, len(nums))))

        if max(nums) <= 0: return max(nums)
        @cache
        def dp(i: int, s: int) -> int:
            ''' Return the max sum from 0 to i'''
            if i <= 0:
                return nums[i] * s
            return max(nums[i] * s + dp(i - 1, s), nums[i] * s)
 
        return max(max(dp(i, 1) for i in range(0, len(nums))), sum(nums) + max(dp(i, -1) for i in range(0, len(nums))))
# @lc code=end

