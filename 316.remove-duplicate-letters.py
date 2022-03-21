#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#

# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        stack = []
        for c in s:
            if not c in stack:
                ascii_no = ord(c)
                while stack and ascii_no < ord(stack[-1]) and counter[stack[-1]] > 0:
                    stack.pop()

                stack.append(c)
            
            counter[c] -= 1
        
        return "".join(stack)

# @lc code=end

