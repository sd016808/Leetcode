#
# @lc app=leetcode id=895 lang=python3
#
# [895] Maximum Frequency Stack
#

# @lc code=start
class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        self.maxFreq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        if self.freq[val] > self.maxFreq:
            self.maxFreq = self.freq[val] 

        self.group[self.freq[val]].append(val)

    def pop(self) -> int:
        val = self.group[self.maxFreq].pop()
        if not self.group[self.maxFreq]:
            self.maxFreq -= 1

        self.freq[val] -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
# @lc code=end

