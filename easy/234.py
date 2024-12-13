# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current = head
        lst = []

        while current:
            lst.append(current.val)
            current = current.next

        if len(lst) == 1:
            return True

        for i in range(len(lst) // 2):
            if lst[i] != lst[-(i + 1)]:
                return False

        return True