#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
from typing import List

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums

        slow = 1
        fast = 1
        while fast < len(nums):
            if nums[fast] <= nums[slow - 1]:
                fast += 1
                continue
            
            nums[slow] = nums[fast]
            slow += 1
            fast += 1
        
        return slow

print(Solution().removeDuplicates([1,1,2,2,3,3,4,5]))


        
# @lc code=end

