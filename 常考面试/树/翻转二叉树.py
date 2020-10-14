# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        def dfs(node):
            if not node:
                return
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

            if node.left or node.right:
                p = node.left
                node.left = node.right
                node.right = p

        dfs(root)
        return root