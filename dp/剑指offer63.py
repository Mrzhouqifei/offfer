class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = []
        n = len(prices)
        if n == 0:
            return 0
        dp.append(0)
        min_price = prices[0]
        max_ans = 0
        for i in range(1, n):
            new_price = prices[i] - min_price
            if new_price > max_ans:
                max_ans = new_price
            elif prices[i] < min_price:
                min_price = prices[i]
        return max_ans
