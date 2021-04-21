"""
单调栈
leetcode 496, 503 下一个更大的元素
556 比当前数大的最小数（位数一样，数字相同）
739 下一个更高的气温，至少需要等待的天数
402. 移掉K位数字
321. 拼接最大数
"""

# 单调递减栈 496
"""
给定两个没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。
nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。
"""
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums2:
            return []
        stack = [nums2[0]]  # 存数（没有重复元素）
        res = {}

        for i in range(1, len(nums2)):
            while stack and nums2[i] > stack[-1]:
                res[stack.pop()] = nums2[i]  # 若遇到更大的元素，则出栈，并判断下一个栈顶元素的大小
            stack.append(nums2[i])

        while stack:    # 栈中剩下的元素都不存在下一个更大的元素
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
        stack = [0]  # 存下标（有重复元素）

        for i in range(1, len(circle)):
            while stack and circle[i] > circle[stack[-1]]:
                res[stack.pop()] = circle[i]  # 若遇到更大的元素，则出栈，并判断下一个栈顶元素的大小
            stack.append(i)
            # if stack[0] >= len(nums):  # 数组所有元素都找到，提前跳出
            #     break
        while stack:  # 栈中剩下的元素都不存在下一个更大的元素
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
                nums[i], nums[cg1] = nums[cg1], nums[i]
                # tmp = nums[i]
                # nums[i] = nums[cg1]
                # nums[cg1] = tmp

                res = int(''.join(nums[:i + 1] + sorted(nums[i + 1:])))
                # if -2 ** 31 < res < 2 ** 31 - 1:
                if res < 2 ** 31 - 1:
                    return res
            stack.append(i)
        return -1

# 739
"""
请根据每日气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，
请在该位置用 0 来代替。
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

"""
给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。

注意:
num 的长度小于 10002 且≥ k。
num 不会包含任何前导零。
示例 1 :
输入: num = "1432219", k = 3
输出: "1219"
解释: 移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219。
"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        # 单调栈
        left_len = len(num) - k
        stack = [num[0]]
        i = 1
        while k and i < len(num):
            while stack and stack[-1] > num[i] and k:
                stack.pop()
                k -= 1
            stack.append(num[i])
            i += 1
        stack = stack + [x for x in num[i:]]
        stack = stack[:left_len]
        res = []
        for i in range(len(stack)):
            if stack[i] != '0':
                res = stack[i:]
                break

        if len(res) == 0:
            return '0'
        return ''.join(res)

"""
给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。现在从这两个数组中选出 k (k <= m + n) 个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。

求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。

说明: 请尽可能地优化你算法的时间和空间复杂度。

示例 1:

输入:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
输出:
[9, 8, 6, 5, 3]
"""
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def merge(A, B):
            i, j = 0, 0
            lenA, lenB = len(A), len(B)
            C = []
            while i < lenA and j < lenB:
                if A[i] > B[j]:
                    C.append(A[i])
                    i += 1
                elif A[i] < B[j]:
                    C.append(B[j])
                    j += 1
                else:
                    strA = [str(x) for x in A[i+1:]]
                    strB = [str(x) for x in B[j+1:]]
                    if ''.join(strA) > ''.join(strB):
                        C.append(A[i])
                        i += 1
                    else:
                        C.append(B[j])
                        j += 1

            C = C + A[i:] + B[j:]
            return C

        def singleMax(nums, n):
            stack = []
            drop = len(nums) - n
            i = 0
            while drop and i < len(nums):
                while stack and drop and nums[i] > stack[-1]:
                    stack.pop()
                    drop -= 1
                stack.append(nums[i])
                i += 1
            stack = stack + nums[i:]
            return stack[:n]

        max_num = '0'
        res = []
        for i in range(1, min(k, len(nums1)) + 1):
            j = k - i
            if j > len(nums2):
                continue
            tmp = merge(singleMax(nums1, i), singleMax(nums2, j))
            strtmp = [str(x) for x in tmp]
            if ''.join(strtmp) > max_num:
                res = tmp
                max_num = ''.join(strtmp)
        return res


