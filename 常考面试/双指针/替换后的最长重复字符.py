"""
leetcode 424 替换后的最长重复字符

给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换k次。在执行上述操作后，找到包含重复字母的最长子串的长度。

注意：字符串长度 和 k 不会超过104。

示例 1：
输入：s = "ABAB", k = 2
输出：4
解释：用两个'A'替换为两个'B',反之亦然。

"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        p1, p2 = 0, 0
        times = [0] * 26
        times[ord(s[p1])- ord('A')] = 1
        res = 0
        while p2 < len(s):
            if max(times) + k >= p2 - p1 + 1:
                res = max(res, p2 - p1 + 1)
                p2 += 1
                if p2 < len(s):
                    times[ord(s[p2]) - ord('A')] += 1
            else:
                times[ord(s[p1]) - ord('A')] -= 1
                p1 += 1
        return res
