#
# @lc app=leetcode id=991 lang=python3
#
# [991] Broken Calculator
#

# @lc code=start
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        count = 0
        while target > startValue:
            if target & 1 > 0:
                target += 1
            else:
                target = target // 2
            count += 1

        return int(count + startValue - target)
# @lc code=end

