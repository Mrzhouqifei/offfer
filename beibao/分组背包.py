"""
分组背包和多重背包很像
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