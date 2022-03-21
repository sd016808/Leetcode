#
# @lc app=leetcode id=946 lang=python3
#
# [946] Validate Stack Sequences
#

# @lc code=start
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = [pushed.pop(0)]
        while popped:
            if stack:
                if stack[-1] == popped[0]:
                    stack.pop()
                    popped.pop(0)
                    continue

            if pushed:
                stack.append(pushed.pop(0))
            else:
                return False
        
        return True
                

            
# @lc code=end

