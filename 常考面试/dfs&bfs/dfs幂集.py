"""
面试题 08.04. 幂集
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = [[]]
        n = len(nums)

        def dfs(tmp, start):
            res.append(tmp)
            if start >= n-1:
                return

            for i in range(start + 1, n):
                tmp_c = tmp + [nums[i]]
                dfs(tmp_c, i)

        for i in range(n):
            dfs([nums[i]], i)
        return res