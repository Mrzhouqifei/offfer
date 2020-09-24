# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:

        # 后续遍历二叉树
        def houxu(node):
            nonlocal num
            if node:
                left = houxu(node.left)
                right = houxu(node.right)
                flag = False
                if left and right:
                    flag = True
                    if node.left:
                        if node.left.val != node.val:
                            flag = False
                    if node.right:
                        if node.right.val != node.val:
                            flag = False
                if flag:
                    num += 1
                return flag
            else:
                return True
        num = 0
        houxu(root)
        return num

