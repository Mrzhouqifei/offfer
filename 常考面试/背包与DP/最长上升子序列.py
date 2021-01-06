"""
leetcode 300
最长上升子序列
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
leetcode 491
上升子序列个数
给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。
"""
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        dp = [[[nums[i]]] for i in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] <= nums[i]:
                    for x in dp[j]:
                        new_x = x.copy()
                        new_x.append(nums[i])
                        dp[i].append(new_x)
        ans = []
        duplicated = set()
        for x in dp:
            for y in x:
                if len(y) >= 2:
                    if str(y) not in duplicated:
                        ans.append(y)
                        duplicated.add(str(y))
        return ans