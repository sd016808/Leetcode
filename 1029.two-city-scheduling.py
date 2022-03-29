#
# @lc app=leetcode id=1029 lang=python3
#
# [1029] Two City Scheduling
#

# @lc code=start
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ans = 0
        costs.sort(key=lambda x:x[0] - x[1])
        for i in range(0, len(costs)//2):
            ans += costs[i][0]

        for i in range(len(costs)//2, len(costs)):
            ans += costs[i][1]
        
        return ans
# @lc code=end

