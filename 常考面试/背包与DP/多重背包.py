n, V = list(map(int, input().split()))
dp = [0] * (V+1)
for i in range(n):
    v, w, s = list(map(int, input().split()))
    for j in range(V, v-1, -1):
        for k in range(1, s + 1):
            if k * v > j:
                break
            dp[j] = max(dp[j], dp[j-k*v] + k*w)
print(dp[-1])