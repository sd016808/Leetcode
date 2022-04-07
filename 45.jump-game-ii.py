#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dp(i: int) -> int:
            if i >= n - 1:
                return 0
            if nums[i] + i >= n - 1 :
                return 1

            res = float('inf')
            for j in range(1, nums[i] + 1):
                res = min(res, dp(i + j))
                
            return res + 1
        
        return dp(0)
# @lc code=end

