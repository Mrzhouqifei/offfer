class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        # f[i][j] = max(f[i-1][j], f[i][j-1]) + grid[i][j]
        m, n = len(grid), len(grid[0])
        f = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                f[i][j] = max(f[i - 1][j], f[i][j - 1]) + grid[i-1][j-1]
        return f[m][n]
    # 数组中的逆序对