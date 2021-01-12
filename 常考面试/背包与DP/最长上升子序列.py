"""
leetcode 300 最长递增子序列

给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。
例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

示例 1：
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if not n:
            return 0
        f = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    f[i] = max(f[i], f[j] + 1)
        return max(f)

"""
leetcode 491 递增子序列
给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。

示例:
输入: [4, 6, 7, 7]
输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
"""

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        dp = [[[nums[i]]] for i in range(len(nums))]
        ans = []
        duplicated = set()
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] <= nums[i]:
                    for x in dp[j]:
                        new_x = x.copy()
                        new_x.append(nums[i])

                        if str(new_x) not in duplicated:
                            ans.append(new_x)
                            dp[i].append(new_x)
                            duplicated.add(str(new_x))
        return ans