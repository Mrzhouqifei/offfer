class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            j = i + 1
            count = 0
            while j < len(nums):
                if nums[i] == nums[j]:
                    if count == 0:
                        count = 1
                        j += 1
                    else:
                        nums.pop(j)
                else:
                    j += 1
            i += 1