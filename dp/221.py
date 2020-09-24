class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        max_ans = 0
        for i in range(m):
            for j in range(n):
                if int(matrix[i][j]) == 1:
                    dp[i][j] = 1
                    if i - 1 >= 0 and j - 1 >= 0:
                        dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                max_ans = max(max_ans, dp[i][j])
        return max_ans ** 2