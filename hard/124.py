# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def calc(node):
            if not node:
                return 0

            left_path_sum = max(calc(node.left), 0)
            right_path_sum = max(calc(node.right), 0)

            max_sum[0] = max(max_sum[0], left_path_sum + right_path_sum + node.val)
            return max(left_path_sum, right_path_sum) + node.val

        max_sum = [root.val]
        calc(root)
        return max_sum[0]
