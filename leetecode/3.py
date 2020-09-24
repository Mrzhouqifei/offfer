class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp = 1
        p = 0
        for i in range(1, n):
            for j in range(p, i):
                if s[j] == s[i]:
                     p = j + 1
                     break
            dp = max(dp, i - p + 1)
        return dp