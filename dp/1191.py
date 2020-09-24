class Solution:
    def kConcatenationMaxSum(self, arr, k: int) -> int:
        if not arr:
            return 0
        mod = 10**9 + 7
        tmp = arr.copy()
        sum_one = sum(tmp)
        if k > 1:
            tmp.extend(tmp)

        def kadane(inputs):
            n = len(inputs)
            dp = [0] * n
            dp[0] = max(0, inputs[0])

            for i in range(1, n):
                dp[i] = max(0, inputs[i], dp[i-1] + inputs[i]) % mod
            return max(dp)

        kadane_ans = kadane(tmp)
        if sum_one <= 0 or k < 2:
            return kadane_ans
        else:
            return kadane_ans + (k - 2) * sum_one






# s = Solution()
# print(s.kConcatenationMaxSum([-1, -2], 7))

arr = [1, 2, 3]
# a = list(map(lambda x: x / abs(x), arr))
arr.extend(arr)
print(arr)
