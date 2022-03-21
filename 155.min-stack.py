#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            min_val = self.getMin()
            if min_val and val < min_val:
                min_val = val

            self.stack.append((min_val, val))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        self.stack.pop() 

    def top(self) -> int:
        min_val, val = self.stack[-1]
        return val

    def getMin(self) -> int:
        min_val, val = self.stack[-1]
        return min_val
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

