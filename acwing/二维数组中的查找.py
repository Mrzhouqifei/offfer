class Solution(object):
    def searchArray(self, array, target):
        """
        :type array: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(array), len(array[0])
        if not m or not n:
            return False
        i = 0
        while i < m:
            if array[i][0] <= target <= array[i][n-1]:
                for j in range(n):
                    if target == array[i][j]:
                        return True
            i += 1
        return False

s = Solution()
s.searchArray([[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]], 15)