class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dicts = {}
        n = len(nums)
        for x in nums:
            if x not in dicts.keys():
                dicts[x] = 1
            else:
                dicts[x] += 1
                if dicts[x] > n / 2:
                    return x