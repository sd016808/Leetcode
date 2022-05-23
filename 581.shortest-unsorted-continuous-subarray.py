#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        start = 0
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                start = i
                break
        else:
            return 0

        end = 0
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] != sorted_nums[i]:
                end = i
                break
        
        return end - start + 1

                
                
# @lc code=end

