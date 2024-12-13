# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def traversal(node):
            if node is None:
                return

            result = traversal(node.left)
            if result is not None:
                return result

            nonlocal k
            k -= 1
            if k == 0:
                return node.val
            
            return traversal(node.right)

        return traversal(root)