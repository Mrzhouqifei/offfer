"""
单调栈
leetcode 496, 503 下一个更大的元素
556 比当前数大的最小数
739
"""

# 单调递减栈 496
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

