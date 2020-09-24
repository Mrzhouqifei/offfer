# class Solution:
#     def generateTrees(self, n: int) -> List[TreeNode]:
#         def generateTrees(start, end):
#             if start > end:
#                 return [None, ]
#
#             allTrees = []
#             for i in range(start, end + 1):  # 枚举可行根节点
#                 # 获得所有可行的左子树集合
#                 leftTrees = generateTrees(start, i - 1)
#
#                 # 获得所有可行的右子树集合
#                 rightTrees = generateTrees(i + 1, end)
#
#                 # 从左子树集合中选出一棵左子树，从右子树集合中选出一棵右子树，拼接到根节点上
#                 for l in leftTrees:
#                     for r in rightTrees:
#                         currTree = TreeNode(i)
#                         currTree.left = l
#                         currTree.right = r
#                         allTrees.append(currTree)
#
#             return allTrees
#
#         return generateTrees(1, n) if n else []


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generateTrees(start, end):
            if start > end:
                return [None]

            all_trees = []

            for i in range(start, end + 1):
                leftTrees = generateTrees(start, i - 1)
                rightTrees = generateTrees(i + 1, end)

                for l in leftTrees:
                    for r in rightTrees:
                        currTree = TreeNode(i)
                        currTree.left = l
                        currTree.right = r
                        all_trees.append(currTree)
            return all_trees

        return generateTrees(1, n) if n else []


