
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
        fast, slow = 1, 0   # 双指针

        while fast < n:
            for i in range(slow, fast):   # 滑动窗口
                if s[i] == s[fast]:
                    slow = i + 1
            dp = max(dp, fast - slow + 1)
            fast += 1
        return dp