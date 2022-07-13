#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#
from functools import cache

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False

        @cache
        def dp(i, sub_s1, sub_s2)-> int:
            if i < 0:
                return 0
            
            maxLength = 0
            if len(sub_s1) > 0 and sub_s1[-1] == s3[i]:
                maxLength = 1 + dp(i-1, sub_s1[:-1], sub_s2)
            
            if len(sub_s2) > 0 and sub_s2[-1] == s3[i]:
                maxLength = max(maxLength, 1 + dp(i-1, sub_s1, sub_s2[:-1]))
            
            return maxLength
        
        return dp(len(s3) - 1, s1, s2)

print(Solution().isInterleave("ab", "bc", "babc"))
            
# @lc code=end

