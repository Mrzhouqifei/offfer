class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        nums = [i for i in range(n)]
        last = 0
        while len(nums) > 1:
            t = m + last
            num_len = len(nums)
            if t > num_len:
                t = t % num_len
            last = t - 1
            nums.pop(t-1)
        return nums[0]