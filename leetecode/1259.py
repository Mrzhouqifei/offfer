# class Solution:
#     def numberOfWays(self, num_people: int) -> int:
#         mod = 10**9 + 7
#         dp = [0] * (num_people+1)
#         dp[0] = 1
#         dp[2] = 1
#         for n in range(4, num_people+1, 2):
#             for j in range(1, n, 2):
#             # for m in range(0, n//2):
#                 j = 2*m + 1
#                 dp[n] += dp[j - 1]*dp[n-j-1]
#
#         return int(dp[num_people] % mod)

print(1e9+7)