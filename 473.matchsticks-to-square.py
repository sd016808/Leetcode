#
# @lc app=leetcode id=473 lang=python3
#
# [473] Matchsticks to Square
#
from typing import List
import heapq 

# @lc code=start
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4:
            return False

        matchsticks.sort(reverse=True)
        totalLength = sum(matchsticks)        
        length = totalLength / 4
        if length != int(length):
            return False
        
        if matchsticks[0] > length:
            return False
            
        edges = [0, 0, 0, 0]
        def backTracking(i):
            if i == len(matchsticks):
                return True
            
            for n in range(4):
                # 重複的不用試
                if n > 0 and edges[n-1] == edges[n]:
                    continue
                # 如果超過長度，不用試
                if edges[n] + matchsticks[i] <= length:
                    edges[n] += matchsticks[i]
                    if backTracking(i+1):
                        return True
                    edges[n] -= matchsticks[i]

            return False
        
        return backTracking(0)
        
        

print(Solution().makesquare([3,3,2,2,2,2,2,2,2,2,2,2,2,2,2]))
# @lc code=end

