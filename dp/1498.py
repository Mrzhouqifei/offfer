class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mod = 10**9 + 7
        nums = sorted(nums)
        left, right = 0, n-1
        ans = 0
        while left <= right:
            if nums[left] + nums[right] <= target:
                ans = (ans + pow(2, right - left)) % mod
                left += 1
            else:
                right -= 1
        return ans