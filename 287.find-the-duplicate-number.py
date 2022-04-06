#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#
# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
            這題限制太難
            參考解法 https://leetcode.com/problems/find-the-duplicate-number/discuss/1892999/Simple-easy-solution-c%2B%2B
        '''
        slow = nums[0]
        fast = nums[0]
        slow = nums[slow]
        fast = nums[nums[fast]]
        while fast!=slow:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = nums[0]
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
        return slow

# @lc code=end

