# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check_range(node, low, high):
            if not node:
                return True 

            if low < node.val < high:
                return check_range(node.left, low, node.val) and check_range(node.right, node.val, high)

            return False

        return check_range(root, -2**31 - 1, 2**31)