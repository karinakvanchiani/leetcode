# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        added_numbers = ListNode((l1.val + l2.val) % 10)
        current = added_numbers
        v_ume = (l1.val + l2.val) // 10
        l1, l2 = l1.next, l2.next

        while l1 and l2:
            s = l1.val + l2.val + v_ume
            current.next = ListNode(s % 10)
            v_ume = s // 10
            l1, l2 = l1.next, l2.next
            current = current.next

        rest = l1 or l2
        while rest:
            s = rest.val + v_ume
            current.next = ListNode(s % 10)
            v_ume = s // 10
            rest = rest.next
            current = current.next

        if v_ume:
            current.next = ListNode(v_ume)
            current = current.next

        return added_numbers