
"""
leetcode 3 无重复字符最长字串
要点：双指针+滑动窗口
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        dp = 1  # 最长字串长度
        p1, p2 = 1, 0   # 双指针

        while p1 < n:
            for i in range(p2, p1):   # 滑动窗口
                if s[i] == s[p1]:
                    p2 = p1 + 1
            dp = max(dp, p1 - p2 + 1)
        return dp