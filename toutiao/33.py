class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0,  len(nums) - 1
        while l <= r:
            mid = (r + l) // 2
            if nums[mid] == target:
                return mid
            elif nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            elif nums[l] < nums[mid]:
                if nums[l] < target < nums[mid]:
                    r = mid - 1
                    l = l + 1
                else:
                    l = mid + 1
                    r = r - 1
            elif nums[mid] < nums[r]:
                if nums[mid] < target < nums[r]:
                    l = mid + 1
                    r = r - 1
                else:
                    r = mid - 1
                    l = l + 1
            else:
                return -1
        return -1