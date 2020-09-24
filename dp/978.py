class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        n = len(A)
        a = [0]
        for i in range(1, len(A)):
            a.append((A[i] > A[i-1]) - (A[i] < A[i-1]))

        dp = [1] * n
        for i in range(1, n):
            if a[i] != 0:
                dp[i] = 2

        for i in range(2, n):
            if a[i] * a[i-1] == -1:
                dp[i] = dp[i-1] + 1
        return max(dp)

                