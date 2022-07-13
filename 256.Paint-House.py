from typing import List

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        @cache
        def dp(houseIndex: int, colorIndex: int):
            '''
            Return the minimum painting cost from 0 to houseIndex end with color index.
            '''        
            if houseIndex < 0:
                return 0
            
            min_val = 10 ** 9
            for i, color in enumerate(costs[houseIndex]):
                if i == colorIndex:
                    continue
                
                min_val = min(min_val, color + dp(houseIndex - 1, i))
            
            return min_val
        
        return dp(len(costs) - 1, -1)

            

print(Solution().minCost([[17,2,17],[16,16,5],[14,3,19]]))