#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# Note P(x) = P(x//2) + x % 2

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        p = [None] * (n + 1)
        p[0] = 0

        for i in range(1, n + 1):
            p[i] = p[i//2] + i % 2

        return p
# @lc code=end

