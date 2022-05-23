#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#

# @lc code=start
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            if num & 1 == 0:
                res.insert(0, num)
            else:
                res.append(num)

        return res
# @lc code=end

