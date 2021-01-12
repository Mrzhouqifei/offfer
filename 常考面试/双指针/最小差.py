"""
面试题 16.06. 最小差
给定两个整数数组a和b，计算具有最小差绝对值的一对数值（每个数组中取一个值），并返回该对数值的差

"""

class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        a = sorted(a)
        b = sorted(b)
        length_a, length_b = len(a), len(b)

        left, right = 0, 0
        ans = float('inf')
        while left < length_a and right < length_b:
            diff = a[left] - b[right]
            if abs(diff) < ans:
                ans = abs(diff)
            if diff < 0:
                left += 1
            else:
                right += 1

        return ans
