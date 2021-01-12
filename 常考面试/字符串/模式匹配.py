"""
面试题 16.18. 模式匹配
你有两个字符串，即pattern和value。 pattern字符串由字母"a"和"b"组成，用于描述字符串中的模式。

示例 1：

输入： pattern = "abba", value = "dogcatcatdog"
输出： true
"""


class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        if not value and len(pattern) <= 1:
            return True
        elif not value or not pattern:
            return False

        count_a = sum(1 for ch in pattern if ch == 'a')
        count_b = len(pattern) - count_a

        if count_a < count_b:  # 保证a > b
            count_a, count_b = count_b, count_a
            pattern = ''.join('a' if ch == 'b' else 'b' for ch in pattern)

        for len_a in range(len(value) // count_a + 1):
            rest = len(value) - count_a * len_a
            if (count_b == 0 and rest == 0) or (count_b != 0 and rest % count_b == 0):
                len_b = 0 if count_b == 0 else rest // count_b
                pos, correct = 0, True
                value_a, value_b = None, None
                for ch in pattern:
                    if ch == 'a':
                        sub = value[pos: pos + len_a]
                        if not value_a:
                            value_a = sub
                        elif value_a != sub:
                            correct = False
                            break
                        pos += len_a
                    else:
                        sub = value[pos: pos + len_b]
                        if not value_b:
                            value_b = sub
                        elif value_b != sub:
                            correct = False
                            break
                        pos += len_b
                if correct and value_a != value_b:
                    return True
        return False