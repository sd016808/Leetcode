#
# @lc app=leetcode id=740 lang=python3
#
# [740] Delete and Earn
#

# @lc code=start
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        counter = Counter(nums)
        array = list(counter.items())
        @cache
        def dp(i: int) -> int:
            if i < 0: return 0
            
            num = array[i][0]
            count = array[i][1]
            score = num * count
            if i - 1 >= 0 and num - 1 != array[i - 1][0]:
                return score + dp(i - 1)
            else:
                return max(score + dp(i - 2), dp(i-1))

        return dp(len(counter.items()) - 1) 

        # 笨方法
        # counter = Counter(sorted(nums))
        # counterList = list(counter.items())
        # dp = [0] * len(counterList)
        # dp[0] = counterList[0][0] * counterList[0][1]
        # for i in range(1, len(counterList)):
        #     if counterList[i][0] > counterList[i-1][0] + 1:
        #         dp[i] = max(dp[i-1], dp[i-2])
        #     else:
        #         if i > 1:
        #             dp[i] = max(dp[i-2], dp[i-3])

        #     dp[i] += counterList[i][0] * counterList[i][1]

        # return max(dp)

# @lc code=end

