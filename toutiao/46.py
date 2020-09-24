class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        used = [0] * n
        def dfs(path):
            if len(path) == n:
                res.append(path.copy())
                return
            else:
                for i in range(n):
                    if used[i]:
                        continue
                    else:
                        used[i] = 1
                        path.append(nums[i])
                        dfs(path)
                        path.pop()
                        used[i] = 0

        dfs([])
        return res
