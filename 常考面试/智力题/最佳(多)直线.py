"""
面试题 16.14. 最佳直线
给定一个二维平面及平面上的 N 个点列表Points，其中第i个点的坐标为Points[i]=[Xi,Yi]。请找出一条直线，其通过的点的数目最多。
设穿过最多点的直线所穿过的全部点编号从小到大排序的列表为S，你仅需返回[S[0],S[1]]作为答案，若有多条直线穿过了相同数量的点，
则选择S[0]值较小的直线返回，S[0]相同则选择S[1]值较小的直线返回。

示例：
输入： [[0,0],[1,1],[1,0],[2,0]]
输出： [0,2]
解释： 所求直线穿过的3个点的编号为[0,2,3]

k = (yi-yj)/(xi-xj)
b = (yi*xj - xi*yj)/(xj-xi)
"""


class Solution:
    def bestLine(self, points: List[List[int]]) -> List[int]:
        dicts_k = {}
        res = [2, 0, 1]
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                if points[i][0] - points[j][0] != 0:    # 斜率存在
                    k = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
                    b = (points[i][1] * points[j][0] - points[i][0] * points[j][1]) / (points[j][0] - points[i][0])
                else:
                    k = '#'
                    b = points[i][0]
                if (k, b) in dicts_k.keys():
                    dicts_k[(k, b)][0] += 1
                else:
                    dicts_k[(k, b)] = [2, i, j]
                if (dicts_k[(k, b)][0] > res[0]) or ((dicts_k[(k, b)][0] == res[0]) and (
                        dicts_k[(k, b)][1] < res[1] or (dicts_k[(k, b)][1] == res[1] and dicts_k[(k, b)][2] < res[2]))):
                    res = dicts_k[(k, b)]
        return res[1:]
