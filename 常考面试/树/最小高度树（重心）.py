
"""
leetcode 310. 最小高度树


示例 1：

输入：n = 4, edges = [[1,0],[1,2],[1,3]]
输出：[1]
解释：如图所示，当根是标签为 1 的节点时，树的高度是 1 ，这是唯一的最小高度树。

"""


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]

        adj = [[] for _ in range(n)]
        degree = [0] * n

        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
            degree[src] += 1
            degree[dst] += 1

        q = [i for i in range(n) if degree[i] == 1]

        while q:
            ans = []

            for i in range(len(q)):
                src = q.pop(0)
                ans.append(src)

                for dst in adj[src]:
                    degree[dst] -= 1
                    if degree[dst] == 1:
                        q.append(dst)
        return ans





