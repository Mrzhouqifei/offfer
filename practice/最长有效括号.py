s="(()"
n = len(s)
dp = [[0 for j in range(n)] for i in range(n)]

for gap in range(1, n):
    i = 0
    while i + gap < n:
        j = i + gap
        if i+1 < n:
            dp[i][j] = max(dp[i][j], dp[i+1][j])
        if j-1>=0:
            dp[i][j] = max(dp[i][j], dp[i][j-1])
        if gap == 1 and s[i] == '(' and s[i + 1] == ')':
            dp[i][j] = 2
        elif (i + 2 < n) and s[i] == '(' and s[i + 1] == ')':
            dp[i][j] = dp[i + 2][j] + 2
        elif j - 2 >= 0 and s[j - 1] == '(' and s[j] == ')':
            dp[i][j] = dp[i][j - 2] + 2
        elif s[i] == '(' and s[j] == ')':
            dp[i][j] = dp[i + 1][j - 1] + 2
        i += 1
print(dp)