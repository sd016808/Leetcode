#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

# @lc code=start
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for stone in stones:
            heappush(h, -stone)

        while len(h) > 1:
            a = heappop(h)
            b = heappop(h)
            z = b - a
            if z != 0:
                heappush(h, -z)
        
        return 0 if not h else -h[0]
        # @lc code=end

