"""
买卖股票的最佳时机
"""
# 121
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice, maxProfit = 999999, 0
        for x in prices:
            if x < minPrice:
                minPrice = x
            elif x - minPrice > maxProfit:
                maxProfit = x - minPrice
        return maxProfit

# 122
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, -prices[0]] for _ in range(n)]

        for i in range(n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[-1][0]