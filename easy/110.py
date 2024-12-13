# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_height(node):
            if not node:
                return 0
    
            if node.left is None and node.right is None:
                return 1
            
            height = 1

            height_l = get_height(node.left)
            height_r = get_height(node.right)

            if abs(height_l - height_r) > 1 or -1 in (height_l, height_r):
                return -1

            height += max(height_l, height_r)
            return height

        return get_height(root) != -1