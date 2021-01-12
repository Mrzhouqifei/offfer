"""
面试题 08.11. 硬币 （完全背包）
硬币。给定数量不限的硬币，币值为25分、10分、5分和1分，编写代码计算n分有几种表示法。
(结果可能会很大，你需要将结果模上1000000007)

示例1:
 输入: n = 5
 输出：2
 解释: 有两种方式可以凑成总金额:
5=5
5=1+1+1+1+1
"""

class Solution:
    def waysToChange(self, n: int) -> int:
        coins = [25, 10, 5, 1]
        dp = [1] + [0] * n
        for coin in coins:
            for j in range(coin, n+1):
                dp[j] = (dp[j] + dp[j - coin]) % 1000000007
        return dp[n]