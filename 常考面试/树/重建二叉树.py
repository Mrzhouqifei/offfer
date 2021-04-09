"""
leetcode 105 前序+中序 重建二叉树

前序遍历 preorder =[3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]
        inorder_index = 0
        for i in range(1, len(preorder)):
            preValue = preorder[i]

            if stack[-1].val != inorder[inorder_index]:
                node = TreeNode(preValue)
                stack[-1].left = node
                stack.append(node)
            else:
                while stack and stack[-1].val == inorder[inorder_index]:
                    node = stack.pop()
                    inorder_index += 1
                node.right = TreeNode(preValue)
                stack.append(node.right)
        return root