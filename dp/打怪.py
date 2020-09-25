"""
去除无法战胜的怪兽，变成0-1背包问题
"""

n, w = list(map(int, input().split()))
A, B = list(map(int, input().split()))
AB = A + B

f = [0] * (w+1)
for i in range(n):
    x, y = list(map(int, input().split()))
    if AB < x:
        continue
    for j in range(w, y - 1, -1):
        f[j] = max(f[j], f[j-y]+1)
print(f[-1])