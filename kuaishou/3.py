k, n = list(map(int, input().split()))
dp = [1 for _ in range(n + 1)]
dp[k] = sum(dp[:k])
for i in range(k+1, n + 1):
    dp[i] = (dp[i - 1] * 2 - dp[i - 1 - k]) % 397
print(dp[-1])