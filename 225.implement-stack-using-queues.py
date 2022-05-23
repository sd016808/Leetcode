#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#

# @lc code=start
class MyStack:

    def __init__(self):
        self.last = None
        self.queue = []
        
    def push(self, x: int) -> None:
        self.queue.append(x)
        self.last = x

    def pop(self) -> int:
        length = len(self.queue)
        if length <= 1:
            self.last = None
        else:
            while length > 1:
                self.last = self.queue.pop(0)
                self.queue.append(self.last)
                length -= 1
        
        return self.queue.pop(0)
    def top(self) -> int:
        return self.last

    def empty(self) -> bool:
        if self.queue:
            return False
        else:
            return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

