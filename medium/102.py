# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        order = []
        children = [root]

        while children:
            level = []
            new_childs = []
            
            for child in children:
                level.append(child.val)

                if child.left:
                    new_childs.append(child.left)
                if child.right:
                    new_childs.append(child.right)

            children = new_childs
            order.append(level)

        return order