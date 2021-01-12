"""
0-1背包
有 N 件物品和一个容量是 V 的背包。每件物品只能使用一次。
第 i 件物品的体积是 vi，价值是 wi。

输入格式
第一行两个整数，N，V，用空格隔开，分别表示物品数量和背包容积。
接下来有 N 行，每行两个整数 vi,wi，用空格隔开，分别表示第 i 件物品的体积和价值。

输出格式
输出一个整数，表示最大价值。
"""
n, V = list(map(int, input().split()))
dp = [0] * (V+1)
for i in range(n):
    v, w = list(map(int, input().split()))
    for j in range(V, v-1, -1):
        dp[j] = max(dp[j], dp[j-v] + w)
print(dp[-1])

"""
完全背包
每种物品都有无限件可用
"""
n, V = list(map(int, input().split()))
dp = [0] * (V+1)
for i in range(n):
    v, w = list(map(int, input().split()))
    for j in range(v, V+1):
        dp[j] = max(dp[j], dp[j-v]+w)
print(dp[-1])

"""
多重背包
第 i 种物品最多有 si 件
"""
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

"""
分组背包 （类似多重背包）
每组物品有若干个，同一组内的物品最多只能选一个。
"""
N, V = list(map(int, input().split()))
f = [0] * (V+1)

for i in range(N):
    s = int(input())
    vw = []
    for k in range(s):
        vw.append(list(map(int, input().split())))

    for j in range(V, -1, -1):
        for k in range(s):
            if j >= vw[k][0]:
                f[j] = max(f[j], f[j-vw[k][0]] + vw[k][1])
print(f[-1])

"""
二维费用背包
体积是 vi，重量是 mi，价值是 wi。
求解将哪些物品装入背包，可使物品总体积不超过背包容量，总重量不超过背包可承受的最大重量，且价值总和最大。
"""

N, V, M = list(map(int, input().split()))
f = [[0] * (M+1) for _ in range(V+1)]  # (V + 1) * (M + 1)

for i in range(N):
    v, m, w = list(map(int, input().split()))
    for j in range(V, v-1, -1):
        for k in range(M, m-1, -1):
            f[j][k] = max(f[j][k], f[j-v][k-m] + w)
print(f[-1][-1])

"""
背包问题求方案数
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