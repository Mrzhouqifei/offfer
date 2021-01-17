"""
39. 组合总和(完全背包)

给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。
说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。
示例 1：

输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = [[] for i in range(target + 1)]
        res_set = [set() for i in range(target + 1)]
        dp = [False] * (target + 1)
        dp[0] = True

        for i in range(len(candidates)):
            for v in range(candidates[i], target + 1):
                if dp[v-candidates[i]]:
                    if not dp[v]:
                        dp[v] = True
                    if len(res[v-candidates[i]]) == 0:
                        res[v].append([candidates[i]])
                    else:
                        for x in res[v-candidates[i]]:
                            new_x = x.copy()
                            new_x.append(candidates[i])
                            if str(new_x) not in res_set:
                                res[v].append(new_x)
                                res_set.append(str(new_x))
        return res[-1]


