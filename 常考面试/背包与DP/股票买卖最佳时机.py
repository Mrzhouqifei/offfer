"""
121 买卖股票的最佳时机
给定一个数组，它的第i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。

示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice, maxProfit = 999999, 0
        for x in prices:
            if x < minPrice:
                minPrice = x
            elif x - minPrice > maxProfit:
                maxProfit = x - minPrice
        return maxProfit

"""
122 买卖股票的最佳时机 II
你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, -prices[0]] for _ in range(n)]

        for i in range(n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[-1][0]