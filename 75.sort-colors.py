#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Quick Sort in-place
        """   
        def partition(start, end):
            if start >= end:
                return

            privot = nums[end]
            nextLeftIdx = start
            for i in range(start, end):
                if nums[i] <= privot:
                    nums[i], nums[nextLeftIdx] = nums[nextLeftIdx], nums[i]
                    nextLeftIdx += 1
            
            nums[end], nums[nextLeftIdx] = nums[nextLeftIdx], nums[end]
            partition(start, nextLeftIdx - 1)
            partition(nextLeftIdx + 1, end)
        
        partition(0, len(nums) - 1)

    def sortColors_bubble(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Bubble Sort
        """
        for j in range(0, len(nums)):
            for i in range (0, len(nums) - j - 1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i+1] = nums[i+1],  nums[i]
    
# @lc code=end

