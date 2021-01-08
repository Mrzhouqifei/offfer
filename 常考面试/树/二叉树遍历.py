"""
94. 二叉树的中序遍历
"""

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def search(node):
            if not node:
                return
            search(node.left)
            res.append(node.val)
            search(node.right)
        search(root)
        return res

"""
面试题 04.05. 合法二叉搜索树
中序遍历
"""

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        inorder =  float('-inf')

        def search(root):
            nonlocal inorder
            if not root:
                return True

            if not search(root.left):
                return False
            if root.val <= inorder:
                return False
            inorder = root.val
            if not search(root.right):
                return False
            return True

        return search(root)
