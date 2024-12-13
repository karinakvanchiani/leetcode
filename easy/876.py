# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        i = 1

        while current:
            current = current.next
            i += 1

        middle = (i - 1) // 2 + 1
        current = head
        node = current

        i = 1
        while current:
            if i == middle:
                node = current
                break
            current = current.next
            i += 1

        return node