class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # odd number 奇数  even number 偶数
        n = len(nums)
        ans, odd = 0, 0
        pre = [0] * (n + 1)

        pre[0] = 1
        for num in nums:
            if num % 2 == 1:
                odd += 1
            if odd >= k:
                ans += pre[odd - k]
            pre[odd] += 1

        return ans
