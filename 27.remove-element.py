#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        
        return i

        # 快慢指標
        # dulplcate = 0
        # slow = 0
        # fast = 0
        # while fast < nums:
        #     if nums[fast] != val:
        #         nums[slow] = nums[fast]
        #         slow += 1
        #     fast += 1
        
        # return slow

            
                
                
# @lc code=end

