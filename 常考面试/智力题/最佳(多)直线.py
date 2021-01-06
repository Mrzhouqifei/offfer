"""
面试题 16.14. 最佳直线
k = (yi-yj)/(xi-xj)
b = (yi*xj - xi*yj)/(xj-xi)
"""

class Solution:
    def bestLine(self, points: List[List[int]]) -> List[int]:
        dicts_k = {}
        res = [2, 0, 1]
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                if points[i][0] - points[j][0] != 0:
                    k = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
                    b = (points[i][1] * points[j][0] - points[i][0] * points[j][1]) / (points[j][0] - points[i][0])
                else:
                    k = '#'
                    b = points[i][0]
                if (k, b) in dicts_k.keys():
                    dicts_k[(k, b)][0] += 1
                else:
                    dicts_k[(k, b)] = [2, i, j]
                if (dicts_k[(k, b)][0] > res[0]) or ((dicts_k[(k, b)][0] == res[0]) and (dicts_k[(k, b)][1] < res[1] or  (dicts_k[(k, b)][1] == res[1] and dicts_k[(k, b)][2] < res[2]))):
                    res = dicts_k[(k, b)]
        return res[1:]


