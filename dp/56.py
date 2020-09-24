class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x: x[0])
        merged = []
        i = 0
        while i < len(intervals):
            tmp = intervals[i]
            mg = tmp
            while i + 1 < len(intervals) and intervals[i+1][0] <= mg[1]:
                mg = [mg[0], max(intervals[i+1][1], mg[1])]
                i += 1
            merged.append(mg)
            i += 1
        return merged




s = Solution()
intervals = [[1,3],[15,18],[2,6],[8,10]]
s.merge(intervals)