# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def treeComparing(tree1, tree2):
            if not tree1 and not tree2:
                return True

            if not tree1 or not tree2:
                return False

            compared1 = treeComparing(tree1.left, tree2.right)
            compared2 = treeComparing(tree2.left, tree1.right)

            return compared1 and compared2 and tree1.val == tree2.val

        return treeComparing(root.left, root.right)
