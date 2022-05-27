#
# @lc app=leetcode id=354 lang=python3
#
# [354] Russian Doll Envelopes
#
from typing import List
from functools import cache

# @lc code=start
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        '''Python 用DP解會TLE，只能用bisect'''
        r = []
        for env in sorted(envelopes, key=lambda x: (x[0], -x[1])):
            pos = bisect.bisect_left(r, env[1])
            if pos==len(r):
                r.append(env[1])
            elif env[1]<r[pos]:
                r[pos] = env[1]
        return len(r)

        # envelopes.sort(key=lambda x: (x[0], -x[1]))
        # @cache
        # def dp(i) -> int:
        #     '''Return Number of envelopes with max width and height'''
        #     if i == 0:
        #         return 1
            
        #     ans = 1
        #     for j in range(i):
        #         if envelopes[i][1] > envelopes[j][1]:
        #             ans = max(ans, dp(j) + 1)
                
        #     return ans
        
        # return max(dp(i) for i in range(len(envelopes)))
        
# @lc code=end

