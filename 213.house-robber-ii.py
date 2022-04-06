#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]

        @cache
        def dp(i: int, j: int) -> int:
            if j < i:   return 0
            return max(dp(i, j - 1), dp(i, j - 2) + nums[j])
        
        return max(dp(0, len(nums) - 2), dp(1, len(nums) - 1))

    # 笨寫法    
    # def rob(self, nums: List[int]) -> int:
    #     if len(nums) <= 3:
    #         return max(nums)

    #     dp = [(0, 0)] * len(nums)
    #     dp[0] = (0, nums[0])
    #     dp[1] = (nums[1], nums[1])
    #     dp[2] = (nums[2] + dp[0][0], nums[2] + dp[0][1])
    #     for i in range(2, len(nums)):
    #         dp[i] = (max(nums[i] + dp[i-2][0], nums[i] + dp[i-3][0]),
    #                     max(nums[i] + dp[i-2][1], nums[i] + dp[i-3][1]))

    #     return max(dp[-1][0], dp[-2][1], dp[-3][1])
# @lc code=end

