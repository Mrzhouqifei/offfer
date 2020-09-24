class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice, maxProfit = 999999, 0
        for x in prices:
            if x < minPrice:
                minPrice = x
            elif x - minPrice > maxProfit:
                maxProfit = x - minPrice
        return maxProfit