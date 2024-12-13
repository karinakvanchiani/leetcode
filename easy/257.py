# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def find_paths(node, paths):
            if not node.left and not node.right:
                return paths.append(node.val)

            if node.left:
                node.left.val = str(node.val) + '->' + str(node.left.val)
                find_paths(node.left, paths)

            if node.right:
                node.right.val = str(node.val) + '->' + str(node.right.val)
                find_paths(node.right, paths)

            return paths

        if not root.left and not root.right:
            return [str(root.val)]

        return find_paths(root, [])