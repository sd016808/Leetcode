#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(i:int) -> int:
            '''
            Return:
            Min Price before i Day
            Max Profit before i Day 
            '''
            if i < 0: return 0, -float('inf')
            if i == 0: return prices[0], 0

            min_price, max_profit = dp(i-1)
            max_profit = max(max_profit, prices[i] - min_price)
            min_price = min(min_price, prices[i])

            return min_price, max_profit

        return dp(len(prices)-1)[1]        

# @lc code=end

