class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        n = len(nums)
        for i1 in range(n-2):
            if i1 > 0 and nums[i1] == nums[i1 - 1]:
                continue
            if nums[i1] > 0:
                break
            i2, i3 = i1 + 1, n-1
            while i2 < i3:
                if nums[i1] + nums[i2] + nums[i3] == 0:
                    res.append([nums[i1], nums[i2], nums[i3]])
                    i2 += 1
                    i3 -= 1
                    while i2 < i3 and nums[i2] == nums[i2-1]: i2 += 1
                    while i3 > i2 and nums[i3] == nums[i3+1]: i3 -= 1

                elif nums[i1] + nums[i2] + nums[i3] > 0:
                    i3 -= 1
                    while i3 > i2 and nums[i3] == nums[i3+1]: i3 -= 1
                else:
                    i2 += 1
                    while i2 < i3 and nums[i2] == nums[i2-1]: i2 += 1
        return res

