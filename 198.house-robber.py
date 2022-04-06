#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(i:int) -> int:
            if i < 0:   return 0
            return max(dp(i-1), dp(i-2) + nums[i])
        
        return dp(len(nums)-1)

        # 笨寫法
        # if len(nums) <= 2:
        #     return max(nums)

        # dp = [0] * len(nums)
        # dp[0] = nums[0]
        # dp[1] = nums[1]
        # dp[2] = dp[0] + nums[2]
        # for n in range(3, len(nums)):
        #     dp[n] = max(dp[n-2],dp[n-3]) + nums[n]

        # return max(dp[-1], dp[-2])
# @lc code=end

