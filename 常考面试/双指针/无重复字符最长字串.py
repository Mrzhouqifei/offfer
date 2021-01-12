
"""
leetcode 3 无重复字符最长字串
要点：双指针 + 滑动窗口

给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
示例 1:

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        dp = 1  # 最长字串长度
        fast, slow = 1, 0   # 双指针

        while fast < n:
            for i in range(slow, fast):   # 判断新增的是否与旧窗口中有重复
                if s[i] == s[fast]:
                    slow = i + 1
            dp = max(dp, fast - slow + 1)
            fast += 1
        return dp