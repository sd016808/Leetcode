#
# @lc app=leetcode id=413 lang=python3
#
# [413] Arithmetic Slices
#

# note: dp[n] = dp[n-1] + 1 if n is match
#       dp[n] = 0           if n not match        


# @lc code=start
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        dp = [0] * len(nums)
        diff = nums[1] - nums[0]
        ans = 0
        for idx in range(2, len(nums)):
            newDiff = nums[idx] - nums[idx - 1]
            if newDiff == diff:
                dp[idx] = dp[idx - 1] + 1
                ans += dp[idx]
            else:
                diff = newDiff

        return ans

# @lc code=end

