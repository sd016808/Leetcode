#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        slow = 0
        fast = 0
        while slow < len(s) and fast < len(t) and len(t) - fast >= len(s) - slow:           
            if t[fast] == s[slow]:
                slow += 1

            fast += 1
        
        return slow == len(s)

# @lc code=end

