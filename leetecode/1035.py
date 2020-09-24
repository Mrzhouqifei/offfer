class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        lena = len(A)
        lenb = len(B)
        dp = [[0]*(lenb+1) for _ in range(lena+1)]
        for i in range(lena):
            for j in range(lenb):
                if A[i] == B[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[lena][lenb]

