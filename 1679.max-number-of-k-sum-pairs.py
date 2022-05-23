#
# @lc app=leetcode id=1679 lang=python3
#
# [1679] Max Number of K-Sum Pairs
#

# @lc code=start
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        ans = 0
        for num in nums:
            if counter[k - num] > 0:
                counter[k - num] -= 1
                ans += 1
            else:
                counter[num] += 1 
        
        return ans
# @lc code=end

