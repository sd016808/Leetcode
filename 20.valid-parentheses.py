#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        rule = {")":"(", "]":"[", "}":"{"}
        stack = []
        for c in s:
            if c in rule:
                if not stack or stack[-1] != rule[c]:
                    return False

                stack.pop()
            else:
                stack.append(c)
        
        return not stack
# @lc code=end

