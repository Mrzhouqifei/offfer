"""
剑指offer32 - I
层次从前到后
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        q, res = [root], []

        while q:
            node = q.pop(0)
            if node:
                res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res


"""
剑指offer32 - II
层次不同列表
"""

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        q, res = [(root, 0)], {}

        while q:
            node, depth = q.pop(0)
            if node:
                if depth in res.keys():
                    res[depth].append(node.val)
                else:
                    res[depth] = [node.val]
                if node.left:
                    q.append((node.left, depth + 1))
                if node.right:
                    q.append((node.right, depth + 1))
        ans = []
        for key in res.keys():
            ans.append(res[key])
        return ans

"""
剑指offer32 - III
之字形
"""

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        q, res = [(root, 0)], {}

        while q:
            node, depth = q.pop(0)
            if node:
                if depth in res.keys():
                    res[depth].append(node.val)
                else:
                    res[depth] = [node.val]
                if node.left:
                    q.append((node.left, depth + 1))
                if node.right:
                    q.append((node.right, depth + 1))
        ans = []
        for key in res.keys():
            if key % 2 == 0:
                ans.append(res[key])
            else:
                ans.append(res[key][::-1])
        return ans
