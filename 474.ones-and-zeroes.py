#
# @lc app=leetcode id=474 lang=python3
#
# [474] Ones and Zeroes
#

# @lc code=start
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counterList = []
        for string in strs:
            counterList.append(Counter(string))
        
        @cache
        def dp(m, n, i):
            '''
            Return max subset counts from zero to i.
            dp(0, 0, i) = 0
            dp(m, n, i) = max(1 + dp(m-counter[i]["0"], n-counter[i]["1"], i - 1),
                              dp[m, n, i - 1])
            '''
            if m == 0 and n == 0:
                return 0

            if m < 0 or n < 0:
                return -1

            if i < 0:
                return 0
            
            new_m = m - counterList[i]["0"]
            new_n = n - counterList[i]["1"]

            return max(1 + dp(new_m, new_n, i - 1), dp(m, n, i - 1))

        return dp(m, n, len(strs) - 1)
            
            
            
# @lc code=end

