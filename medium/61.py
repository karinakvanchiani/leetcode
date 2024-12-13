# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k == 0:
            return head

        curr = head
        i = 1
        while curr.next:
            curr = curr.next
            i += 1

        k %= i
        if k == 0:
            return head
            
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy
        i = 0

        while fast.next:
            fast = fast.next

            if i >= k:
                slow = slow.next

            i += 1

        tmp = slow.next
        slow.next = None
        fast.next = dummy.next
        return tmp