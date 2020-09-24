class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int: #: List[List[int]]
        n = len(triangle)
        dp = [[0] * n for _ in range(n)]
        if not triangle:
            return 0
        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            for j in range(i+1):
                if j == i:
                    dp[i][j] = triangle[i][j] + dp[i - 1][j-1]
                elif j - 1 >= 0:
                    dp[i][j] = triangle[i][j] + min(dp[i-1][j-1], dp[i-1][j])
                else:
                    dp[i][j] = triangle[i][j] + dp[i - 1][j]
        print(dp)
        return min(dp[n-1])

s = Solution()
s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
