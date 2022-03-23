#
# @lc app=leetcode id=1663 lang=python3
#
# [1663] Smallest String With A Given Numeric Value
#

# @lc code=start
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        stack = [None] * n
        for i in range(0, n):
            tmp = k - (n - i - 1) * 26
            if tmp <= 0:
                stack[i] = "a"
                k -= 1
            else:
                stack[i] = chr(tmp + 96)
                k -= tmp
        
        return "".join(stack)
# @lc code=end

