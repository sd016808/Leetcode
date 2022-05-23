#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        isNegtive = x < 0
        
        if x < 0:
            isNegtive = True
            x = -x

        if x == 0:
            return 0

        digits = int(log10(x)) + 1
        ans = 0
        i = 1
        while i <= digits:
            ans +=  (x % 10) * 10 ** (digits - i)
            i += 1
            x //= 10
            if ans > 2 ** 31 - 1:
                return 0
        return ans if not isNegtive else -ans

# @lc code=end

