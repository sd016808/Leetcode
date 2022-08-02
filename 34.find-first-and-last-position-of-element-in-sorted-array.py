from typing import List
import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        left = bisect.bisect_left(nums,target)
        if left >= len(nums) or nums[left] != target:
            return [-1, -1]
        
        right = bisect.bisect_right(nums[left:],target)
        return [left, right + left - 1]
        
        # def searchLeft(nums, target):
        #     left = 0
        #     right = len(nums) - 1
        #     while left <= right:
        #         mid = (right + left) // 2
        #         if nums[mid] < target:
        #             left = mid + 1
        #         else:
        #             right = mid - 1
            
        #     return left
        
        # def searchRight(nums, target, left):
        #     right = len(nums) - 1
        #     while left <= right:
        #         mid = (right + left) // 2
        #         if nums[mid] <= target:
        #             left = mid + 1
        #         else:
        #             right = mid - 1
            
        #     return right

        # left = searchLeft(nums, target)
        # if left == len(nums) or nums[left] != target:
        #     return [-1, -1]

        # right = searchRight(nums, target, left)
        # return [left, right]

print(Solution().searchRange([2, 2], 3))