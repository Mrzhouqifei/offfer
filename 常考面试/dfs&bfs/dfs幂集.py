"""
面试题 08.04. 幂集
幂集。编写一种方法，返回某集合的所有子集。集合中不包含重复的元素。

 输入： nums = [1,2,3]
 输出：
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
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