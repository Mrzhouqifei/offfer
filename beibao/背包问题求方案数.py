"""
求一定容量下总方案数就是简单的0-1背包转换，sum
求一定容量下最优方案方案总数
"""
N, V = list(map(int, input().split()))
f = [0] * (V+1)
g = [1] * (V+1)
mod = 10**9 + 7

for i in range(N):
    v, w = list(map(int, input().split()))
    for j in range(V, v - 1, -1):
        if f[j-v] + w > f[j]:
            f[j] = f[j-v] + w
            g[j] = g[j-v]
        elif f[j-v] + w == f[j]:
            g[j] = (g[j] + g[j - v]) % mod
print(g[-1])