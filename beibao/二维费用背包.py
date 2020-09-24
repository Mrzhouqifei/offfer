"""
二维费用背包
"""

N, V, M = list(map(int, input().split()))
f = [[0] * (M+1) for _ in range(V+1)]  # (V + 1) * (M + 1)

for i in range(N):
    v, m, w = list(map(int, input().split()))
    for j in range(V, v-1, -1):
        for k in range(M, m-1, -1):
            f[j][k] = max(f[j][k], f[j-v][k-m] + w)
print(f[-1][-1])