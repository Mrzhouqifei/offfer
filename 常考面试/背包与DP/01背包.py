n, V = list(map(int, input().split()))
dp = [0] * (V+1)
for i in range(n):
    v, w = list(map(int, input().split()))
    for j in range(V, v-1, -1):
        dp[j] = max(dp[j], dp[j-v] + w)
print(dp[-1])
        