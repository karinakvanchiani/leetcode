# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None

        dummy = ListNode(0, head)
        slow, fast = dummy, dummy
        i = 0

        while fast.next:
            fast = fast.next

            if i >= n:
                slow = slow.next

            i += 1

        slow.next = slow.next.next
        return dummy.next