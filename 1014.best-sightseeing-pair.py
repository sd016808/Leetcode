#
# @lc app=leetcode id=1014 lang=python3
#
# [1014] Best Sightseeing Pair
#

# @lc code=start
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # score = values[i] + values[j] + i - j
        #       = (values[i] + i) +  (values[j] - j)
        @cache
        def dp(i: int) -> int:
            '''Return Max first part score ended with i'''
            if i == 0:
                return values[i]
            
            return max(values[i] + i, dp(i - 1))
        
        return max(dp(i - 1) + values[i] - i for i in range(1, len(values)))

        

# @lc code=end

