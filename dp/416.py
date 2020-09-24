class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        avg = int(sum(nums) / 2)
        dp = [False] * (avg + 1)
        dp[0] = True
        for i in range(len(nums)):
            if dp[avg]:
                    return True
            for j in range(avg, nums[i]-1, -1):
                dp[j] = dp[j] or dp[j-nums[i]]
        return False