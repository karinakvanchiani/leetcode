# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        childs = [root]
        n = len(childs)
        depth = 0

        while childs:
            child = childs[0]
            childs = childs[1:]

            if child.left:
                childs.append(child.left)
            if child.right:
                childs.append(child.right)

            n -= 1

            if n == 0:
                depth += 1
                n = len(childs)

        return depth