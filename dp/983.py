class Solution:
    def mincostTickets(self, days, costs) -> int:
        if not days:
            return 0
        n = days[-1] + 1
        dp = [0] * n
        dp[days[0]] = min(costs)

        i, j = days[0] + 1, 1
        while j < len(days):
            while j > 0 and i < days[j]:
                dp[i] = dp[days[j-1]]
                i += 1
            if i - 30 >= 0:
                dp[i] = min(dp[i-1] + costs[0], dp[i-7] + costs[1], dp[i-30] + costs[2])
            elif i - 7 >= 0:
                dp[i] = min(dp[i - 1] + costs[0], dp[i - 7] + costs[1], costs[2])
            else:
                dp[i] = min(dp[i - 1] + costs[0], costs[1], costs[2])
            i += 1
            j += 1
        return dp[n-1]

s = Solution()
days = [1,4,6,7,8,20]
costs = [2,7,15]
s.mincostTickets(days, costs)