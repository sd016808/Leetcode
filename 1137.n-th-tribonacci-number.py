#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#

# @lc code=start
class Solution:
    @cache
    def tribonacci(self, n: int) -> int:
        if n <= 1: return n
        elif n == 2: return 1
        else: return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
# @lc code=end

