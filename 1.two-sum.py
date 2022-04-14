#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i, num in enumerate(nums):
            if target - num in cache:
                return [i, cache[target - num]]
            
            cache[num] = i
        
        return []
# @lc code=end

