#
# @lc app=leetcode id=1567 lang=python3
#
# [1567] Maximum Length of Subarray With Positive Product
#

# @lc code=start
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        
        @cache
        def dp(i: int) -> Tuple[int, int]:
            """Max length of pos/neg product subarray ends with nums[i]."""
            if i < 0 or nums[i] == 0:
                return 0, 0
            
            pos, neg = dp(i - 1)
            if nums[i] > 0:
                return  1 + pos, 1 + neg if neg > 0 else 0
            else:
                return 1 + neg if neg > 0 else 0, pos + 1
        
        return max(dp(i)[0] for i in range(len(nums)))
# @lc code=end

