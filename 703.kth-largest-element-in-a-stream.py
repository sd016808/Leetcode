#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#

# @lc code=start
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapify(self.heap)
        self.__decreaseTok()

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        self.__decreaseTok()
        return self.heap[0]
    
    def __decreaseTok(self):
        while len(self.heap) > self.k:
            heappop(self.heap)

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

