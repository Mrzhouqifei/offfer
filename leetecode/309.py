class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        hold, cool, sell = [0] * n, [0] * n, [0] * n
        hold[0] = -prices[0]
        for i in range(1, n):
            sell[i] = hold[i - 1] + prices[i]
            hold[i] = max(hold[i - 1], cool[i-1] - prices[i])
            cool[i] = max(cool[i - 1], sell[i - 1])
        return max(sell[n-1], cool[n - 1])