"""
无向树的直径 leetcode 1245
N叉树的直径 leetcode 1522
"""

"""
无向树的直径 leetcode 1245
给你这棵「无向树」，请你测算并返回它的「直径」：这棵树上最长简单路径的 边数。
我们用一个由所有「边」组成的数组 edges来表示一棵无向树，其中edges[i] = [u, v]表示节点u 和 v之间的双向边。
树上的节点都已经用{0, 1, ..., edges.length}中的数做了标记，每个节点上的标记都是独一无二的。
"""
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        edges_len = len(edges)
        nodes = [[] for _ in range(edges_len+1)]
        for edge in edges:
            nodes[edge[0]].append(edge[1])
            nodes[edge[1]].append(edge[0])

        def DFS(last, end, length):
            nonlocal max_length, last_node
            if length > max_length:
                max_length = length
                last_node = end
            for next in nodes[end]:
                if next != last:
                    DFS(end, next, length + 1)
        max_length, last_node = 0, 0
        DFS(-1, 0, 0)
        new_start = last_node
        max_length, last_node = 0, 0
        DFS(-1, new_start, 0)
        return max_length


"""
给定一棵 N 叉树的根节点 root ，计算这棵树的直径长度。
N 叉树的直径指的是树中任意两个节点间路径中 最长 路径的长度。这条路径可能经过根节点，也可能不经过根节点。
（N 叉树的输入序列以层序遍历的形式给出，每组子节点用 null 分隔）

思路：
深度优先搜索返回高度（叶节点高度为1），搜索过程中需要取两个最大高度的子节点，他们的高度和即为把此节点作为“中心”时的直径。
对所有节点做同样操作，最后找出最大直径。当子节点个数小于两个时，需要注意用0补位。

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""


class Solution:
    def diameter(self, root: 'Node') -> int:
        self.res = 0
        def dfs(root):
            r = [0, 0]
            if root:
                for child in root.children:
                    r.append(dfs(child))
                r.sort(reverse=True)
            self.res = max(self.res, sum(r[:2]))
            return r[0] + 1
        dfs(root)
        return self.res



