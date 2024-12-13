# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        order = []
        children = [root]
        true_childs = children

        while children:
            order.append([child.val for child in children])
            children = []

            for child in true_childs:
                if child.left:
                    children.append(child.left)
                if child.right:
                    children.append(child.right)

            true_childs = children
            children = children[::-1] if len(order) % 2 == 1 else children
        return order