"""
单调栈
leetcode 496, 503 下一个更大的元素
556 比当前数大的最小数
739
"""

# 单调递减栈 496
"""
给定两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。
nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。
"""
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums2:
            return []
        stack = [nums2[0]]  # 存数
        res = {}

        for i in range(1, len(nums2)):
            while stack and nums2[i] > stack[-1]:
                res[stack.pop()] = nums2[i]
            stack.append(nums2[i])

        while stack:
            res[stack.pop()] = -1

        ans = []
        for num in nums1:
            ans.append(res[num])
        return ans

# 503
"""
给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组遍历顺序，
这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。
"""
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        circle = nums + nums
        res = {}
        stack = [0]  # 存下标

        for i in range(1, len(circle)):
            while stack and circle[i] > circle[stack[-1]]:
                res[stack.pop()] = circle[i]
            stack.append(i)
            if stack[0] >= len(nums):
                break
        while stack:
            res[stack.pop()] = -1
        ans = []
        for i in range(len(nums)):
            ans.append(res[i])
        return ans

# 556
# 12443111
# 从后往前维护一个单调递增栈
"""
给定一个32位正整数 n，你需要找到最小的32位整数，其与 n 中存在的位数完全相同，并且其值大于n。如果不存在这样的32位整数，则返回-1。
"""
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        stack = [len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            cg1 = -1
            while stack and nums[i] < nums[stack[-1]]:
                cg1 = stack.pop()
            if cg1 != -1:
                tmp = nums[i]
                nums[i] = nums[cg1]
                nums[cg1] = tmp

                res = int(''.join(nums[:i + 1] + sorted(nums[i + 1:])))
                if -2 ** 31 < res < 2 ** 31 - 1:
                    return res
            stack.append(i)
        return -1

# 739
"""
请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。
"""
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T:
            return []
        res = [0] * len(T)
        stack = [0]
        for i in range(1, len(T)):
            while stack and T[i] > T[stack[-1]]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res

