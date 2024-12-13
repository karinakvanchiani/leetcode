# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def add_nodes(start, end):
            if start > end:
                return None

            mid = (start + end) // 2
            root = TreeNode(nums[mid])
            root.left = add_nodes(start, mid - 1)
            root.right = add_nodes(mid + 1, end)
            return root

        return add_nodes(0, len(nums) - 1)