class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        pre = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                pre[i][j] = pre[i-1][j] + pre[i][j-1] - pre[i-1][j-1] + mat[i-1][j-1]

        ans = [[0] * (n) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = pre[min(i+K+1, m)][min(j+K+1, n)] + pre[max(i-K, 0)][max(j-K, 0)] - \
                            pre[min(i+K+1, m)][max(j-K, 0)] - pre[max(i-K, 0)][min(j+K+1, n)]
        return ans