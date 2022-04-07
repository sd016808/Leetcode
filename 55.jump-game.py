#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

from typing import List

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        stepIndex = len(nums) - 1
        for idx in range(len(nums) - 2, -1, -1):
            if nums[idx] + idx >= stepIndex:
                stepIndex = idx
        
        return stepIndex == 0

    # 從頭找的版本，很慢
    # def canJump(self, nums: List[int]) -> bool:
    #     @cache
    #     def dp(i: int) -> bool:
    #         if i >= len(nums) - 1:
    #             return True

    #         if nums[i] == 0:
    #             return False
            
    #         if nums[i] >= len(nums) - 1 - i:
    #             return True

    #         for j in range(nums[i], 0, -1):
    #             if dp(i + j):
    #                 return True

    #         return False
    #     return dp(0)
# @lc code=end

