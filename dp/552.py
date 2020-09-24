"""
class Solution {
public:
    int checkRecord(int n) {
        long dp[2][3][n+1];   //dp[i][j][k]表示有i个A,结尾是连续j个L,长度为k的字符串所代表的组合数
        memset(dp,0,sizeof(dp));
        dp[0][0][1] = 1;
        dp[1][0][1] = 1;
        dp[0][1][1] = 1;

        for(int len = 2 ; len <= n ; ++len){
            dp[0][0][len] = (dp[0][0][len-1] + dp[0][1][len-1] + dp[0][2][len-1] )% 1000000007;
            dp[1][0][len] = (dp[0][0][len-1] + dp[0][1][len-1] + dp[0][2][len-1] + dp[1][0][len-1] + dp[1][1][len-1] + dp[1][2][len-1])% 1000000007;
            dp[0][1][len] = dp[0][0][len-1]% 1000000007;
            dp[1][1][len] = dp[1][0][len-1]% 1000000007;
            dp[0][2][len] = dp[0][1][len-1]% 1000000007;
            dp[1][2][len] = dp[1][1][len-1]% 1000000007;
        }
        return (dp[0][0][n] + dp[1][0][n] + dp[0][1][n] + dp[1][1][n] + dp[0][2][n] + dp[1][2][n]) % 1000000007;
    }
};
"""


class Solution:
    def checkRecord(self, n: int) -> int:
        dp = [[[0] * (n + 1) for i in range(3)] for j in range(2)]
        # dp[i][j][k] i几个A, j末尾几个L，k几位
        dp[0][0][1] = 1
        dp[0][1][1] = 1
        dp[1][0][1] = 1

        mod = 10 ** 9 + 7
        for k in range(2, n + 1):
            dp[0][0][k] = (dp[0][0][k - 1] + dp[0][1][k - 1] + dp[0][2][k - 1]) % mod
            dp[0][1][k] = dp[0][0][k - 1] % mod
            dp[0][2][k] = dp[0][1][k - 1]
            dp[1][0][k] = (dp[0][0][k - 1] + dp[0][1][k-1] + dp[0][2][k-1] + dp[1][0][k - 1] + dp[1][1][k - 1] + dp[1][2][k - 1]) % mod
            dp[1][1][k] = dp[1][0][k - 1]
            dp[1][2][k] = dp[1][1][k - 1]

        return (dp[0][0][n] + dp[0][1][n] + dp[0][2][n] + dp[1][0][n] + dp[1][1][n] + dp[1][2][n]) % mod