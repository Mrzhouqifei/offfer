# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int] 前序遍历
        :type inorder: List[int] 中序遍历
        :rtype: TreeNode
        """
        self.pos = {}
        n = len(preorder)
        for i in range(n):
            self.pos[inorder[i]] = i
        return self.dfs(preorder, inorder, 0, n-1, 0, n-1)

    def dfs(self, preorder, inorder, pl, pr, il, ir):
        if pl > pr: return None
        k = self.pos[preorder[pl]] - il
        root = TreeNode(preorder[pl])
        root.left = self.dfs(preorder, inorder, pl+1, pl+k, il, il+k-1)
        root.right = self.dfs(preorder, inorder, pl+k+1, pr, il+k+1, ir)
        return root

