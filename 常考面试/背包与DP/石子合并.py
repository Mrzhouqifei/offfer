n = int(input())
stones = list(map(int, input().split()))
s = [0]
for x in stones:
    s.append(s[-1] + x)
f = [[0] * n for _ in range(n)]


for len in range(2, n+1):
    for i in range(n - len + 1):
        j = len + i - 1
        f[i][j] = float('inf')
        for k in range(i, j):
            f[i][j] = min(f[i][j], f[i][k] + f[k+1][j] + s[j+1] - s[i])

print(f[0][n-1])