class Solution:
    def canPartitionKSubsets(self, nums, k: int) -> bool:
        sums = sum(nums)
        if sums % k != 0:
            return False
        else:
            nums = sorted(nums, reverse=True)
            avg = int(sums / k)
            if nums[-1] > avg:
                return False
            else:
                visited = [0] * len(nums)
                def dfs(k, start, sum_now):
                    if k == 1:
                        return True
                    elif sum_now == avg:
                        # print(k-1)
                        dfs(k-1, 0, 0)
                    else:
                        for i in range(start, len(nums)):
                            if visited[i] == 0 and sum_now + nums[i] <= avg:
                                visited[i] = 1
                                if dfs(k, i+1, sum_now + nums[i]):
                                    return True
                                visited[i] = 0
                        return False
                return dfs(k, 0, 0)


s = Solution()
print(s.canPartitionKSubsets([10,10,10,7,7,7,7,7,7,6,6,6], 3))


    # def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
    #     if not nums or len(nums) < k:  # 为空或不够分
    #         return False
    #     avg, mod = divmod(sum(nums), k)
    #     if mod:  # 不能整除
    #         return False
    #     nums.sort(reverse=True)  # 倒序排列
    #     if nums[0] > avg:  # 有超过目标的元素
    #         return False
    #     used = set()  # 记录已使用的数
    #
    #     def dfs(k, start=0, tmpSum = 0):  # 当前还需要凑的avg个数，当前从哪个数开始考虑，以及当前已凑够的和
    #         if tmpSum == avg:  # 如果已凑满一个
    #             return dfs(k-1, 0, 0)  # 那么从最大数重新开始考虑，凑下一个
    #         if k == 1:  # 只剩最后一个，那么剩下的没使用的数加起来肯定凑满
    #             return True
    #         for i in range(start, len(nums)):  # 优先用大的数的凑
    #             if i not in used and nums[i]+tmpSum <= avg:  # 如果该数未使用并且可以用来凑
    #                 used.add(i)  # 使用该数
    #                 if dfs(k, i+1, nums[i]+tmpSum):  # 继续用比该数小的数来凑
    #                     return True
    #                 used.remove(i)  # 没有得到可用方案，则换个数来凑
    #         return False
    #
    #     return dfs(k)
