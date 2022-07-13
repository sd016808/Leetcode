#
# @lc app=leetcode id=1473 lang=python3
#
# [1473] Paint House III
#
from typing import List
from functools import cache

# @lc code=start
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], target: int) -> int:
        @cache
        def dp(i: int, j:int, g:int):
            '''
            Return the minCost from 0 to i house and painting with g groups.
            i: house index
            j: painting color index
            g: remain groups
            '''
            if i < 0:
                return 0 if g == 0 else float("inf")
            
            if g == 0:
                if houses[i] != 0:
                    if houses[i] - 1 != j:
                        return float("inf")
                    else:
                        return dp(i-1, j, g)
                else:
                    return cost[i][j] + dp(i-1, j, g)
            else:
                if houses[i] != 0:
                    if houses[i] - 1 == j:
                        return dp(i-1, houses[i] - 1, g)
                    else:
                        return dp(i-1, houses[i] - 1, g - 1)
                else:
                    min_cost = float("inf")
                    for index, color_cost in enumerate(cost[i]):
                        if index == j:
                            min_cost = min(min_cost, color_cost + dp(i-1, index, g))
                        else:
                            min_cost = min(min_cost, color_cost + dp(i-1, index, g - 1))
                    
                    return min_cost
        
        return dp(len(houses) - 1, -1, target)

print(Solution().minCost([0,0,0,1], [[1,5],[4,1],[1,3],[4,4]], 4))

# @lc code=end

